#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/path-sum-iii/description/

# O(n) solution
# https://leetcode.com/problems/path-sum-iii/discuss/91892/Python-solution-with-detailed-explanation


# Normally we'll need to select both end of a range, so that the complexity is O(n^2)
# But this problem we don't want to count every possible range, we just need to find out the ranges
# that sums up to a `target` number. That results in another solution

# 1. calculate the prefix sum: root->A, root->B, root->C
# 2. Instead of storing the sequence of numbers, we actually want to count the occurrences of the
#    numbers. Say root -> A(1) -> B(O) -> C(2). then root->B equals to root->C.
# 3. Now say we met new child D. we want to check the path that ends with D has the length `target`
#    a) A naive way is to check root->D, A->D, B->D, C->D, D->D one by one. Results in O(n^2) again.
#    b) Note that we can check how many paths exists whose length is (root->D - target)
#    Thus only O(1) is needed to count the number of pathes that ends with D meet the requirements.

# I was trying to solve a more general problem, but it turns out we need the problem specific
# condition to optimize

from util import TreeNode

class Solution(object):
    def pathSum(self, root, sum):
        return self.inner(root, sum, 0, {0:1})

    def inner(self, root, target, sofar, counts):
        if not root:
            return 0

        ret = 0
        complement = sofar + root.val - target
        if complement in counts:
            ret += counts[complement]

        sofar += root.val
        counts.setdefault(sofar, 0) # consider root.val is 0, what happens?
        counts[sofar] += 1
        ret += self.inner(root.left, target, sofar, counts)
        ret += self.inner(root.right, target, sofar, counts)
        counts[sofar] -= 1
        return ret

solution = Solution()
assert solution.pathSum(TreeNode.of([10,5,-3,3,2,None,11,3,-2,None,1]), 8) == 3
