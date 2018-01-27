#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/house-robber/description/

class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        rob_current = 0
        not_rob_current = 0

        for num in nums:
            new_not_rob_current = max(rob_current, not_rob_current)
            new_rob_current = not_rob_current + num
            rob_current = new_rob_current
            not_rob_current = new_not_rob_current
        return max(rob_current, not_rob_current)
