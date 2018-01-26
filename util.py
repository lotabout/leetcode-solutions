#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def as_list(self):
        lst = []
        node = self
        while node is not None:
            lst.append(node.val)
            node = node.next
        return lst
    
    def __eq__(self, obj):
        if isinstance(obj, ListNode):
            return obj.val == self.val and obj.next == self.next
        elif isinstance(obj, list):
            return self.as_list() == obj

    def __repr__(self):
        return "ListNode" + str(self.as_list())

    @staticmethod
    def of(lst):
        last = head = ListNode(None)
        for item in lst:
            last.next = ListNode(item)
            last = last.next
        return head.next
