class solution():

    def __init__(self, aSudoku, size=9):
        self.sudoku_size = size
        self.sudoku = aSudoku
        self.lines = self.__lines()
        self.columns = self.__columns()
        self.cells = self.__cells()

    def __lines(self):
        result = []
        for line in self.sudoku.splitlines():
            result.append([
                int(number)
                for number in line.split()
            ])
        return result

    def __columns(self):
        result = []
        for i in range(self.sudoku_size):
            result.append([
                line[i]
                for line in self.lines
            ])

        return result

    def __cells(self):
        result = []
        for j in range(self.sudoku_size - 2):
            for i in range(self.sudoku_size - 2):
                if i % 3 == 0 and j % 3 == 0:
                    result.append(
                        self.lines[j + 0][i:i+3] +
                        self.lines[j + 1][i:i+3] +
                        self.lines[j + 2][i:i+3]
                    )
        return result

    def is_valid(self, anArrayOfNumbers):
        return len(set(anArrayOfNumbers)) == self.sudoku_size

    def is_correct(self):
        for line in self.lines:
            if not self.is_valid(line):
                return False

        for column in self.columns:
            if not self.is_valid(column):
                return False

        for cell in self.cells:
            if not self.is_valid(cell):
                return False

        return True
