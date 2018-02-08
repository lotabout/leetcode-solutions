#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/friend-circles/description/

class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """

        visited = [False] * len(M)

        ret = 0
        for i in range(len(M)):
            if not visited[i]:
                ret += 1
                self.paint_circle(M, i, visited)
        return ret

    def paint_circle(self, M, p, visited):
        visited[p] = True

        for i, friend in enumerate(M[p]):
            if not friend:
                continue

            if not visited[i]:
                self.paint_circle(M, i, visited)

solution = Solution()
assert solution.findCircleNum([[1,1,0], [1,1,1], [0,1,1]]) == 1
