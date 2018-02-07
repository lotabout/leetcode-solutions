#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/diameter-of-binary-tree/description/

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root is None:
            return 0

        return self.inner(root)[0]-1
        
    def inner(self, root):
        """return (max_diameter, max_depth)"""
        if root is None:
            return (0, 0)

        l_diameter, l_depth = self.inner(root.left)
        r_diameter, r_depth = self.inner(root.right)
        return (max(l_diameter, r_diameter, l_depth+r_depth+1) , max(l_depth, r_depth)+1)

from util import TreeNode
solution = Solution()
assert solution.diameterOfBinaryTree(TreeNode.of([1,2,3,4,5])) == 3
