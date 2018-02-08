#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/subtree-of-another-tree/description/

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """

        if s is None and t is None:
            return True
        elif s is None or t is None:
            return False

        return self.equals(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)


    def equals(self, s, t):
        if s is None and t is None:
            return True
        elif s is None or t is None:
            return False

        return s.val == t.val and self.equals(s.left, t.left) and self.equals(s.right, t.right)

from util import TreeNode
solution = Solution()
assert solution.isSubtree(TreeNode.of([3,4,5,1,2]), TreeNode.of([4,1,2]))
assert not solution.isSubtree(TreeNode.of([3,4,5,1,2,None,None,0]), TreeNode.of([4,1,2]))
assert solution.isSubtree(TreeNode.of([1,None,1,None,1,None,1,None,1,None,1,None,1,None,1,None,1,None,1,None,1,2]), TreeNode.of([1,None,1,None,1,None,1,None,1,None,1,2]))
