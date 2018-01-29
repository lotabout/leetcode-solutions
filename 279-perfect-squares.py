#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/perfect-squares/description/

import math

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.numSquaresWithCache(n)

    def numSquaresWithCache(self, n, cache={}):
        if n in cache:
            return cache[n]
        sqrt = int(math.sqrt(n))
        if sqrt * sqrt == n:
            cache[n] = 1
            return 1

        square_nums = [i*i for i in range(1, sqrt + 1)]
        
        min_squares = n
        for square in reversed(square_nums):
            num = self.numSquares(n-square)
            if num + 1 < min_squares:
                min_squares = num + 1

        cache[n] = min_squares
        return min_squares




solution = Solution()
assert solution.numSquares(12) == 3
assert solution.numSquares(13) == 2
assert solution.numSquares(7691) == 3
