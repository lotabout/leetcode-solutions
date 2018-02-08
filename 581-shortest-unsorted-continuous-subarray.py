#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/description/

class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0

        prefix_max = [nums[0]]
        for num in nums[1:]:
            prefix_max.append(max(prefix_max[-1], num))

        postfix_min = [nums[-1]]
        for num in reversed(nums[:-1]):
            postfix_min.append(min(postfix_min[-1], num))
        postfix_min = postfix_min[::-1]

        start = 0
        for i in range(len(nums)):
            if nums[i] > postfix_min[i]:
                start = i
                break

        end = -1
        for i in range(len(nums)-1,-1,-1):
            if nums[i] < prefix_max[i]:
                end = i
                break

        # print(start, end, prefix_max, postfix_min, nums)

        return end-start+1

solution = Solution()
assert solution.findUnsortedSubarray([]) == 0
assert solution.findUnsortedSubarray([1]) == 0
assert solution.findUnsortedSubarray([1,2]) == 0
assert solution.findUnsortedSubarray([1,2,3]) == 0
assert solution.findUnsortedSubarray([1,3,2]) == 2
