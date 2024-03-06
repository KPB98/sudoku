class Sudoku:
    valid_set = set(range(1,10))

    def __init__(self, board: list):
        self.board = [[0 if element == "." else int(element) for element in row] for row in board]

    def legit(self):
        return self.row_check() and self.column_check() and self.cube_check()

    def row_check(self):
        for row in self.board:
            for element in row:
                if element in Sudoku.valid_set and row.count(element) > 1:
                    return False
        return True

    def column_check(self):
        c_to_r = Sudoku([[row[i] for row in self.board] for i in range(len(self.board))]).row_check()
        return c_to_r

    def cube_check(self):
        for l in range(0,9,3):
            for k in range(0,9,3):
                cube_dict = {}
                cube = [[self.board[i+l][j+k] for j in range(3)] for i in range(3)]
                for row in cube:
                    for element in row:
                        if element in Sudoku.valid_set:
                            if element not in cube_dict:
                                cube_dict[element] = 1
                            else:
                                return False
            print(cube_dict)
        return True