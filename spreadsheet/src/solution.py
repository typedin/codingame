
def get_arg_val(arg, cells):
    if "$" in arg:
        return cells[int(arg.replace("$", ''))]
    elif "_" in arg:
        return 0
    else:
        return int(arg)


def perform_operation_on_cell(operation, arg1, arg2, cells):
    if operation == "VALUE":
        return get_arg_val(arg1, cells)
    if operation == "ADD":
        return get_arg_val(arg1, cells) + get_arg_val(arg2, cells)
    if operation == "SUB":
        return get_arg_val(arg1, cells) - get_arg_val(arg2, cells)
    if operation == "MULT":
        return get_arg_val(arg1, cells) * get_arg_val(arg2, cells)
    raise ValueError("operator was not understood")


def evalutate_dependencies(cells, in_deps, out_deps, cell_operations):
    ready_cells = set()
    evaluated_cells = set()

    for cell in out_deps:
        if not out_deps[cell]:
            ready_cells.add(cell)

    def removed_dependency(cell, in_deps, out_deps):
        if cell not in in_deps:
            return []

        result = []
        for index in in_deps[cell]:
            if cell in out_deps[index]:
                out_deps[index].remove(cell)
            if not out_deps[index]:
                result.append(index)

        return result

    def array_from_dependencies_only(cell, in_deps, out_deps, evaluated_cells):
        return [
            o
            for o in removed_dependency(cell, in_deps, out_deps)
            if o not in evaluated_cells
        ]

    while ready_cells:
        cell = ready_cells.pop()
        evaluated_cells.add(cell)
        cells[cell] = perform_operation_on_cell(
            **cell_operations[cell],
            cells=cells
        )
        ready_cells.update(
            array_from_dependencies_only(
                cell,
                in_deps,
                out_deps,
                evaluated_cells
            )
        )

    return cells


def enrich_operation(aReading):
    return {
        'operation': aReading[0],
        'arg1': aReading[1],
        'arg2': aReading[2],
    }


def evaluate_reference(arg, aCellOperation):
    return int(aCellOperation[arg][1:])


def cell_operations_from_readings(readings):
    result = [{} for _ in range(nb_cells(readings))]

    for cell in range(int(nb_cells(readings))):
        result[cell] = enrich_operation(readings[cell + 1].split())

    return result


def add_dependency_for_reference(cell, in_deps, out_deps, cell_operations):
    def add_arg_cell_to_out_deps(cell, out_deps, arg_cell):
        if cell not in out_deps:
            out_deps[cell] = set()
        out_deps[cell].add(arg_cell)

    def add_arg_cell_to_in_deps(cell, in_deps, arg_cell):
        if arg_cell not in in_deps:
            in_deps[arg_cell] = set()
        in_deps[arg_cell].add(cell)

    for arg in ["arg1", "arg2"]:
        if '$' in cell_operations[cell][arg]:
            add_arg_cell_to_out_deps(
                cell,
                out_deps,
                evaluate_reference(arg, cell_operations[cell]),
            )
            add_arg_cell_to_in_deps(
                cell,
                in_deps,
                evaluate_reference(arg, cell_operations[cell]),
            )


def nb_cells(readings):
    return int(readings[0])


def create_dependencies(readings, in_deps, out_deps):
    def set_cell_to_out_dependency(cell, out_deps):
        if cell not in out_deps:
            out_deps[cell] = set()

    # def set_cell_to_in_dependency(arg_cell, in_deps):
        # if arg_cell not in in_deps:
            # in_deps[arg_cell] = set()

    for cell in range(nb_cells(readings)):
        set_cell_to_out_dependency(
            cell,
            out_deps
        )
        add_dependency_for_reference(
            cell,
            in_deps,
            out_deps,
            cell_operations_from_readings(readings)
        )
    pass


def solution(readings):
    in_deps = {}
    out_deps = {}
    cells = [0] * nb_cells(readings)

    create_dependencies(readings, in_deps, out_deps)

    return evalutate_dependencies(
        cells,
        in_deps,
        out_deps,
        cell_operations_from_readings(readings)
    )
