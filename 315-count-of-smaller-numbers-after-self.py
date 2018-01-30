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


class TreeNode(object):
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val
        self.count = 1
        self.left_tree_size = 0

    def insert(self, val):
        if self.val == val:
            self.count += 1
            return self.left_tree_size
        elif val < self.val:
            self.left_tree_size += 1
            if self.left is None:
                self.left = TreeNode(val)
                return 0
            return self.left.insert(val)

        # right child
        if self.right is None:
            self.right = TreeNode(val)
            return self.count + self.left_tree_size

        return self.count + self.left_tree_size + self.right.insert(val)

class Solution(object):
    def countSmaller(self, nums):
        if not nums:
            return []

        ret = [0]
        root = TreeNode(nums[-1])
        for n in reversed(nums[:-1]):
            ret.append(root.insert(n))

        return ret[::-1]

solution = Solution()
assert solution.countSmaller([5,2,6,1]) == [2,1,1,0]
assert solution.countSmaller([-1,-1]) == [0, 0]
