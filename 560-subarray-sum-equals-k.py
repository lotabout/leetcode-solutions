#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/subarray-sum-equals-k/description/

# I think it is a sub-problem of: https://leetcode.com/problems/path-sum-iii/description/

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        counts = {0:1}
        sofar = 0
        ret = 0

        for num in nums:
            sofar += num
            complement = sofar - k

            ret += counts.get(complement, 0)

            counts.setdefault(sofar, 0)
            counts[sofar] += 1

        return ret

solution = Solution()
assert solution.subarraySum([1,1,1], 2) == 2
