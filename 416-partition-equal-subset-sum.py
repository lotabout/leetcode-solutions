#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# TLE
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        total = sum(nums)
        if total & 1:
            return False

        possibilities = self.get_all_possibles(nums)
        return total//2 in possibilities

    def get_all_possibles(self, nums):
        if not nums:
            return set(0)
        elif len(nums) == 1:
            return set([nums[0], 0])

        mid = len(nums) // 2
        left_results = self.get_all_possibles(nums[:mid])
        right_results = self.get_all_possibles(nums[mid:])
        return set([a+b for a in left_results for b in right_results])


class Solution(object):
    def canPartition(self, nums):
        total = sum(nums)
        if total & 1:
            return False

        dp = set([0])
        for num in nums:
            dp.update([x+num for x in dp])
        return total // 2 in dp

        
solution = Solution()
assert solution.canPartition([1, 5, 11, 5])
assert not solution.canPartition([1,2,3,5])
assert solution.canPartition([35,69,8,10,56,85,20,67,39,15,57,19,80,45,12,81,92,98,25,26,51,3,31,16,30,37,55,52,61,17,30,82,52,85,84,83,98,29,79,29,99,70,97,20,42,22,44,44,65,75,70,86,97,100,45,69,91,53,88,96,65,88,92,73,16,57,34,11,64,3,92,48,98,29,39,16,47,92,22,19,50,86,78,68,52,51,70,80,2,58,79,70,91,94,23,47,81,4,18,15])
