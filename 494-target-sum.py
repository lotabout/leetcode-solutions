#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/target-sum/description/

from collections import defaultdict

# TLE
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if not nums:
            return 0

        maxsum = sum(nums)

        dp = defaultdict(lambda: 0)

        dp[(0, -nums[0])] += 1
        dp[(0, nums[0])] += 1

        for i in range(1, len(nums)):
            for j in range(-maxsum, maxsum+1):
                dp[(i,j)] = dp[(i-1,j-nums[i])] + dp[(i-1, j+nums[i])]

        return dp[(len(nums)-1, S)]

# basically the same with the above, but use array to reduce the access cost
class Solution(object):
    def findTargetSumWays(self, nums, S):
        if not nums:
            return 0

        maxsum = sum(nums)

        if S > maxsum:
            return 0

        dp = [[0 for _ in range(2*maxsum+1)] for _ in range(len(nums))]

        dp[0][nums[0] + maxsum] += 1
        dp[0][-nums[0] + maxsum] += 1

        for i in range(1, len(nums)):
            for j in range(2*maxsum+1):
                if j-nums[i] >= 0:
                    dp[i][j] += dp[i-1][j-nums[i]]
                if j+nums[i] < len(dp[0]):
                    dp[i][j] += dp[i-1][j+nums[i]]

        # print(f"  {[i for i in range(len(dp[0]))]}")
        # for i in range(len(dp)):
            # print(f"{i} {dp[i]}")

        return dp[len(nums)-1][S+maxsum]


solution = Solution()
assert solution.findTargetSumWays([1, 1, 1, 1, 1], 3) == 5
assert solution.findTargetSumWays([0,0,0,0,0,0,0,0,1], 1) == 256
assert solution.findTargetSumWays([2,7,9,13,27,31,37,3,2,3,5,7,11,13,17,19,23,29,47,53], 107) == 0
assert solution.findTargetSumWays([1], 2) == 0
