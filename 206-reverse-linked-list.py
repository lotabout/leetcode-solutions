#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from util import ListNode

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head is None:
            return head
        
        cur = head
        prev = None
        while cur is not None:
            nxt = cur.next
            cur.next = prev

            prev = cur
            cur = nxt
        return prev

x = ListNode.of([1,2,3,4])
solution = Solution()
y = solution.reverseList(x)
assert y == [4,3,2,1]
