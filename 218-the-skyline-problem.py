#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/the-skyline-problem/description/

import heapq

# follow this:
# https://leetcode.com/problems/the-skyline-problem/discuss/61209/
class Solution:
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """

        points = sorted(set([a for l, r, _ in buildings for a in [l, r]]))

        heap = [] # heap of (-H, R)
        ret = []
        i = 0

        for pt in points:
            # remove the buildings that falls behind (start from tall buildings)
            # note that not all buildings that fall behind will be removed, only the ones that will
            # affect the calculation will be removed: the ones that are taller than current max and
            # had falled behind
            while heap and heap[0][1] <= pt:
                heapq.heappop(heap)

            # include new buildings
            while i < len(buildings) and buildings[i][0] == pt:
                heapq.heappush(heap, (-buildings[i][2], buildings[i][1]))
                i += 1

            height = -heap[0][0] if heap else 0
            if not ret or ret[-1][1] != height:
                ret.append([pt, height])

        return ret







buildings = [[2,9,10], [3,7,15], [5,12,12], [15,20,10], [19,24,8]]
solution = Solution()
print(solution.getSkyline(buildings))
