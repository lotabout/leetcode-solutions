#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/merge-two-binary-trees/description/

from util import TreeNode

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """

        if t1 is None and t2 is None:
            return None
        
        root = TreeNode(0)
        if t1:
            root.val += t1.val
        if t2:
            root.val += t2.val

        root.left = self.mergeTrees(t1.left if t1 else None, t2.left if t2 else None)
        root.right = self.mergeTrees(t1.right if t1 else None, t2.right if t2 else None)
        return root

solution = Solution()
assert solution.mergeTrees(TreeNode.of([1,3,2,5]), TreeNode.of([2,1,3,None,4,None,7])) == [3,4,5,5,4,None,7]
