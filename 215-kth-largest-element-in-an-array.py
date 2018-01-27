#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/kth-largest-element-in-an-array/description/

# Learnt quick select from the discussions
# there is actually an algorithm that achieve O(n) in worst case, but I think quick select is quite
# interesting to implement

class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        left = 0
        right = len(nums) - 1
        k -= 1

        while True:
            pivot_index = (left + right) // 2
            mid = self.partition(nums, pivot_index, left, right)
            if mid == k:
                return nums[k]
            elif mid > k:
                right = mid - 1
            else:
                left = mid + 1

    def partition(self, nums, pivot_index, left, right):
        # return the index where all right(inclusive) number are <= nums[pivot_index]

        if left >= right:
            return left

        pivot_val = nums[pivot_index]
        self.swap(nums, pivot_index, right)
        stored_index = left
        for i in range(left, right):
            if nums[i] > pivot_val:
                self.swap(nums, stored_index, i)
                stored_index += 1
        self.swap(nums, stored_index, right)
        return stored_index

    def swap(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

solution = Solution()
nums = [3,2,1,5,6,4]
assert solution.findKthLargest(nums, 1) == 6
assert solution.findKthLargest(nums, 2) == 5
assert solution.findKthLargest(nums, 3) == 4
assert solution.findKthLargest(nums, 4) == 3
assert solution.findKthLargest(nums, 5) == 2
assert solution.findKthLargest(nums, 6) == 1

solution = Solution()
nums = [3,2,1,5,4]
assert solution.findKthLargest(nums, 1) == 5
assert solution.findKthLargest(nums, 2) == 4
assert solution.findKthLargest(nums, 3) == 3
assert solution.findKthLargest(nums, 4) == 2
assert solution.findKthLargest(nums, 5) == 1

solution = Solution()
nums = [3]
assert solution.findKthLargest(nums, 1) == 3
