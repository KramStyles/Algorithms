from random import randint
from ssl import match_hostname


class Matrix:
    def __init__(self):
        self.matrix = []

    def initialise_matrix(self, size):
        """
        Generates an n x n matrix based on the `size` passed in as parameter.
        For example: if size = 3, then a 3 by 3 matrix would be generated.
        """
        for row in range(0, size):
            self.matrix.append([])
            for col in range(0, size):
                value = randint(0, 99)
                self.matrix[row].append(value)
        return self.matrix

    def display_matrix(self):
        """
        Displays the square matrix as a 2D grid.
        """
        length = len(self.matrix)
        for row in range(0, length):
            st = "| "
            for col in range(0, length):
                if self.matrix[row][col] < 10:
                    st = st + str(self.matrix[row][col]) + "  | "
                else:
                    st = st + str(self.matrix[row][col]) + " | "
            print(st)

    def calculate_diagonal_diff(self):
        ans = []
        ans2 = []
        for index, mat in enumerate(self.matrix):
            back = (len(self.matrix) - index) - 1
            ans2.append(mat[back])
            ans.append(mat[index])
        return ("The diagnonal difference is ", abs(sum(ans2) - sum(ans)))

    def calculate_corner_sum(self):
        ans = self.matrix
        return sum([ans[0][0], ans[0][-1], ans[-1][0], ans[-1][-1]])


matrix = Matrix()
matrix.initialise_matrix(5)
matrix.display_matrix()
print(matrix.calculate_diagonal_diff())
print(matrix.calculate_corner_sum())
