#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class BinaryIndexedTree(object):
    def __init__(self, n):
        self.sums = [0] * (n + 1)

    def sum(self, i):
        ret = 0
        while i > 0:
            ret += self.sums[i]
            i -= i & (-i)
        return ret

    def update(self, i, delta = 1):
        while i < len(self.sums):
            self.sums[i] += delta
            i += i & (-i)

# the key is to map the array to [1..n]

class Solution(object):
    def countSmaller(self, nums):
        if not nums:
            return []
        hashes = {v: i+1 for i, v in enumerate(sorted(nums))}

        ret = []
        tree = BinaryIndexedTree(len(nums))
        for n in reversed(nums):
            ret.append(tree.sum(hashes[n]))
            tree.update(hashes[n]+1)
        return ret[::-1]
        
solution = Solution()
assert solution.countSmaller([5,2,6,1]) == [2,1,1,0]
assert solution.countSmaller([-1,-1]) == [0, 0]
