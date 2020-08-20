def difference(length_fence, arr):
    if len(arr) == 1:
        if arr[0][0] != 0:
            yield [0, arr[0][0]]
        if arr[0][1] != length_fence:
            yield [arr[0][1], length_fence]

    if len(arr) > 1:
        for i in range(len(arr)):
            if i == 0:
                if arr[0][0] != 0:
                    yield [0, arr[0][0]]
                yield [arr[0][1], arr[1][0]]
            if arr[i][1] != length_fence:
                if i == len(arr) - 1:
                    yield [arr[i][1], length_fence]
                elif 0 < i < len(arr) - 1:
                    yield [arr[i][1], arr[i + 1][0]]


def merge(arr):
    sorted_arr = sorted(arr)
    merged = []

    def appendTupleToMerge(anArray):
        merged.append(tuple(anArray))

    def mergedOverlapping(previous, current):
        return (previous[0], max(previous[1], current[1]))

    for current_range in sorted_arr:
        if not merged:
            appendTupleToMerge(current_range)
            continue

        previous_range = merged.pop()

        if previous_range[1] >= current_range[0]:
            appendTupleToMerge(mergedOverlapping(
                previous_range, current_range))
            continue
        appendTupleToMerge(previous_range)
        appendTupleToMerge(current_range)

    return merged


def solution(readings):
    readings = readings.splitlines()

    painted_sections = merge([
        [
            int(line.split()[0]),
            int(line.split()[1]),
        ]
        for line in readings[2:]
    ])

    return [i for i in difference(int(readings[0]), painted_sections)]
