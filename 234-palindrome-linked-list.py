#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/palindrome-linked-list/description/

# The O(n) time O(1) request is quite meaningless in my point of view, but still it is a good
# problem to practice coding skills

from util import ListNode

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return True

        length = 0
        node = head
        while node is not None:
            length += 1
            node = node.next

        # reverse the linked list
        prev = None
        cur  = head
        for _ in range(length//2):
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        p1 = front_head = prev
        p2 = tail_head = cur

        if length % 2 == 1:
            p2 = p2.next

        ret = True
        while p1 is not None and p2 is not None:
            if p1.val != p2.val:
                ret = False
                break
            p1 = p1.next
            p2 = p2.next

        # revert back
        prev = tail_head
        cur = front_head
        while cur is not None:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return ret

solution = Solution()

x = ListNode.of([1,2,3,2,1])
assert solution.isPalindrome(x)
assert x == [1,2,3,2,1]

y = ListNode.of([1,2,2,1])
assert solution.isPalindrome(y)
assert y == [1,2,2,1]

z = ListNode.of([])
assert solution.isPalindrome(z)
