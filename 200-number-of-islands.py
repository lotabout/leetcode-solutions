#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0

        rows = len(grid)
        cols = len(grid[0])

        num_of_islands = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    num_of_islands += 1
                    self.dfs(grid, r, c)
        return num_of_islands
        
    def dfs(self, grid, r, c):
        rows = len(grid)
        cols = len(grid[0])

        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
            return

        grid[r][c] = '0'
        for dr, dc in ((-1, 0), (0, -1), (0, 1), (1, 0)):
            self.dfs(grid, r+dr, c+dc)
