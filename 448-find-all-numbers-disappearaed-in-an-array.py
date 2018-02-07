#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

# I think the "no extra space" limit is basically not possible to achieve if we do not modify the
# input array.

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        for i in range(len(nums)):
            target = abs(nums[i])-1
            if nums[target] > 0:
                nums[target] = -nums[target]

        ret = [i for i in range(1,len(nums)+1) if nums[i-1] > 0]

        # restore
        for i in range(len(nums)):
            nums[i] = abs(nums[i])

        return ret

solution = Solution()
assert solution.findDisappearedNumbers([4,3,2,7,8,2,3,1]) == [5, 6]
        
