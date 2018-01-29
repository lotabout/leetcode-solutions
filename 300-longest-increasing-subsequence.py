#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0

        dp = [1] * len(nums)

        for i in range(len(nums)-1,-1,-1):
            for j in range(i-1,-1,-1):
                if nums[j] < nums[i]:
                    dp[j] = max(dp[j], dp[i] + 1)

        return max(dp)

solution = Solution()
assert solution.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4


