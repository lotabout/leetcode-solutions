#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        ret = [1]
        for n in nums:
            ret.append(ret[-1] * n)

        acc = 1
        for i in range(len(ret)-1, 0, -1):
            ret[i] = ret[i-1]*acc
            acc *= nums[i-1]
        return ret[1:]

solution = Solution()
assert solution.productExceptSelf([1,2,3,4]) == [24,12,8,6]
