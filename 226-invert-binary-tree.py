#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/invert-binary-tree/description/

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        if root is None:
            return

        self.invertTree(root.left)
        self.invertTree(root.right)
        tmp = root.left
        root.left = root.right
        root.right = tmp
