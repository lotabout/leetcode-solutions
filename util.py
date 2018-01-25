#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def to_list(self):
        lst = []
        node = self
        while node is not None:
            lst.append(node.val)
            node = node.next
        return lst

    def __repr__(self):
        return str(self.to_list())

    @staticmethod
    def of(lst):
        last = head = ListNode(None)
        for item in lst:
            last.next = ListNode(item)
            last = last.next
        return head.next
