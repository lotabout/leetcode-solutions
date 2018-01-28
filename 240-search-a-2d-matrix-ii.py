#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/search-a-2d-matrix-ii/description/

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False

        rows = len(matrix)
        cols = len(matrix[0])
        return self.search(matrix, 0, rows-1, 0, cols-1, target)

    def search(self, matrix, rt, rb, cl, cr, target):
        if rt > rb or cl > cr:
            return False
        rm = (rt + rb) // 2
        cm = (cl + cr) // 2
        if matrix[rm][cm] == target:
            return True
        elif matrix[rm][cm] < target:
            # right half, bottom left
            region = [(rt,rb,cm+1,cr), (rm+1,rb,cl,cm)]
            return any([self.search(matrix, rt, rb, cl, cr, target) for rt, rb, cl, cr in region])
        else:
            # top half, bottom left
            region = [(rt,rm-1,cl,cr), (rm,rb,cl,cm-1)]
            return any([self.search(matrix, rt, rb, cl, cr, target) for rt, rb, cl, cr in region])

matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
solution = Solution()
assert solution.searchMatrix(matrix, 5)
assert not solution.searchMatrix(matrix, 20)
