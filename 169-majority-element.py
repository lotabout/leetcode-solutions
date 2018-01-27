#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # naive solution that counts every number
        min_num = len(nums) // 2
        counts = {}

        for n in nums:
            current_count = counts.get(n, 0) + 1
            counts[n] = current_count
            if current_count > min_num:
                return n
            
lst = [1,1,2]
solution = Solution()
assert solution.majorityElement(lst) == 1


# O(1) space
# like two armies, one army take advantage in numbers

class Solution2:
    def majorityElement(self, nums):
        ret = None
        num = 0

        for n in nums:
            if num == 0:
                ret = n
                num = 1
            elif ret == n:
                num += 1
            else:
                num -= 1
        return ret
