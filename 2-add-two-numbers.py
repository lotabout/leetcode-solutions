#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from util import ListNode

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        last = head = ListNode(0)
        carry = 0
        n1 = l1
        n2 = l2

        while n1 is not None and n2 is not None:
            val = carry + n1.val + n2.val
            last.next = ListNode(val % 10)
            carry = val // 10

            last = last.next
            n1 = n1.next
            n2 = n2.next

        if n1 is None and n2 is None:
            rest = None
        elif n1 is None:
            rest = n2
        else:
            rest = n1

        while rest is not None:
            val = carry + rest.val
            last.next = ListNode(val % 10)
            carry = val // 10

            last = last.next
            rest = rest.next

        if carry != 0:
            last.next = ListNode(carry)

        return head.next

solution = Solution()
l1 = ListNode.of([2,4,3])
l2 = ListNode.of([5,6,4])
assert solution.addTwoNumbers(l1, l2).to_list() == [7, 0, 8]

l1 = ListNode.of([2,4])
l2 = ListNode.of([5,6,4])
assert solution.addTwoNumbers(l1, l2).to_list() == [7, 0, 5]

l1 = ListNode.of([2,4])
l2 = ListNode.of([5])
assert solution.addTwoNumbers(l1, l2).to_list() == [7, 4]

l1 = ListNode.of([0])
l2 = ListNode.of([0])
assert solution.addTwoNumbers(l1, l2).to_list() == [0]
