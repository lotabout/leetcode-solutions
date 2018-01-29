#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import deque

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


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def serialize(self):
        result = []
        q = deque([self])
        while q:
            root = q.pop()
            if root:
                result.append(root.val)
                q.appendleft(root.left)
                q.appendleft(root.right)
            else:
                result.append(None)

        while result and result[-1] is None:
            result.pop()

        return result

    @staticmethod
    def of(data):
        if data == '':
            return None

        root = TreeNode(data[0])
        q = deque([root])
        idx = 1

        while idx < len(data):
            node = q.pop()
            left = data[idx]
            right = data[idx+1]
            idx += 2
            if left is not None:
                node.left = TreeNode(left)
                q.appendleft(node.left)
            if right is not None:
                node.right = TreeNode(right)
                q.appendleft(node.right)

        return root

    def __repr__(self):
        return "TreeNode" + str(self.serialize())
