#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/house-robber-iii/description/

from util import TreeNode

# Naive, TLE
class Solution(object):
    def rob(self, root, parent_robbed=False):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        vals = []
        if parent_robbed:
            vals.append(self.rob(root.left, False) + self.rob(root.right, False))
        else:
            vals.append(root.val + self.rob(root.left, True) + self.rob(root.right, True))
            vals.append(self.rob(root.left, False) + self.rob(root.right, False))
        return max(vals)

# Cached, AC
class Solution(object):
    def rob(self, root, parent_robbed=False, cache={}):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        if (root, parent_robbed) in cache:
            return cache[(root, parent_robbed)]

        vals = []
        if parent_robbed:
            vals.append(self.rob(root.left, False, cache) + self.rob(root.right, False, cache))
        else:
            vals.append(root.val + self.rob(root.left, True, cache) + self.rob(root.right, True, cache))
            vals.append(self.rob(root.left, False, cache) + self.rob(root.right, False, cache))
        ret = max(vals)
        cache[(root, parent_robbed)] = ret
        return ret



solution = Solution()
assert solution.rob(TreeNode.of([3,2,3,None,3,None,1])) == 7
assert solution.rob(TreeNode.of([3,4,5,1,3,None,1])) == 9
