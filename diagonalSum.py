class Solution(object):
    def diagonalSum(self, mat):
        diagonals = []
        n = len(mat)
        total_sum = 0

        for i in range(n):
            for j in range(n):
                if i == j or i + j == n - 1:
                    diagonals.append(mat[i][j])

        for value in diagonals:
            total_sum += value

        return total_sum
