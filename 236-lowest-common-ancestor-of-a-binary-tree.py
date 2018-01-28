#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        return self.findNodeOrRoot(root, p, q)


    def findNodeOrRoot(self, root, p ,q):
        if root is None:
            return None

        left = self.findNodeOrRoot(root.left, p, q)
        right = self.findNodeOrRoot(root.right, p, q)

        if root == p or root == q:
            return root
        elif left is not None and right is not None:
            return root
        else:
            return left if left is not None else right
