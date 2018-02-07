#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/convert-bst-to-greater-tree/description/

from util import TreeNode

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        return self.rec(root, 0)[1]

    def rec(self, root, sum):
        if root is None:
            return (sum, None)

        total, r = self.rec(root.right, sum)
        new_root = TreeNode(root.val + total)
        new_total, l = self.rec(root.left, new_root.val)
        new_root.left = l
        new_root.right = r
        return (new_total, new_root)

solution = Solution()
assert solution.convertBST(TreeNode.of([5,2,13])) == [18,20,13]
assert solution.convertBST(TreeNode.of([2,0,3,-4,1])) == [5,6,3,2,6]
