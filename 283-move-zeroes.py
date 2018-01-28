#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        p = 0
        while p < len(nums) and nums[p] != 0:
            p += 1

        q = p+1
        while q < len(nums):
            if nums[q] != 0:
                nums[p] = nums[q]
                p += 1
            q += 1

        while p < len(nums):
            nums[p] = 0
            p += 1
