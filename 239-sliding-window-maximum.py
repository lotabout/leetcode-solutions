#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/sliding-window-maximum/description/

from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        if not nums or k == 0:
            return []

        queue = MonotoneQueue()
        for n in nums[:k]:
            queue.push(n)

        ret = [queue.max()]
        for i in range(k, len(nums)):
            queue.push(nums[i])
            queue.pop(nums[i-k])
            ret.append(queue.max())
        return ret

class MonotoneQueue:
    def __init__(self):
        self.queue = deque()

    def push(self, x):
        while self.queue and self.queue[-1] < x:
            self.queue.pop()
        self.queue.append(x)

    def pop(self, x):
        if self.queue[0] == x:
            self.queue.popleft()

    def max(self):
        return self.queue[0] if len(self.queue) > 0 else None

solution = Solution()
assert solution.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3) == [3,3,5,5,6,7]
assert solution.maxSlidingWindow([-7,-8,7,5,7,1,6,0], 4) == [7,7,7,7,7]
