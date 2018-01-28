#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        if not matrix:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])

        dp = [[0 for _ in row] for row in matrix]

        for i in range(rows):
            dp[i][0] = 1 if matrix[i][0] == "1" else 0
        for j in range(cols):
            dp[0][j] = 1 if matrix[0][j] == "1" else 0

        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == "0":
                    continue

                square = min(dp[i-1][j], dp[i][j-1])
                if matrix[i-square][j-square] == "1":
                    square += 1
                dp[i][j] = square

        max_square_length = max([max(row) for row in dp])
        return max_square_length * max_square_length

matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
solution = Solution()
assert solution.maximalSquare(matrix) == 4
