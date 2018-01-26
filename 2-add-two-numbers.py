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

class Solution2(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        last = head = ListNode(0)
        carry = 0

        while l1 or l2 or carry != 0:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            last.next = ListNode(carry % 10)
            last = last.next
            carry = carry // 10

        return head.next
            
import unittest

class MyTests(unittest.TestCase):
    # (l1, l2, result)
    cases = (([2,4,3], [5,6,4], [7,0,8]),
             ([2,4], [5,6,4], [7, 0, 5]),
             ([2,4], [5], [7, 4]),
             ([0], [0], [0]))

    def setUp(self):
        self.solution = Solution()

    def test_2_add(self):
        for case in self.cases:
            l1, l2, result = case
            n1 = ListNode.of(l1)
            n2 = ListNode.of(l2)
            res = ListNode.of(result)
            self.assertEqual(self.solution.addTwoNumbers(n1, n2), res)

class MyTests2(MyTests):
    def setUp(self):
        self.solution = Solution2()
        

if __name__ == '__main__':
    unittest.main()
