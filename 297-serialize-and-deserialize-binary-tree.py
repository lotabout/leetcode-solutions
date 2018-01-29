#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/

# recursive would be easier, level order is harder

from util import TreeNode

from collections import deque

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        result = []
        if root is None:
            return ''

        q = deque([root])
        while q:
            root = q.pop()
            if root:
                result.append(root.val)
                q.appendleft(root.left)
                q.appendleft(root.right)
            else:
                result.append(None)

        return ','.join(map(str, result))

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == '':
            return None

        data = list(map(lambda x: None if x == 'None' else int(x), data.split(',')))

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

c = Codec()
data = "1,2,3,None,None,4,5,None,None,None,None"
assert c.serialize(c.deserialize(data)) == data

data = "1,None,None"
assert c.serialize(c.deserialize(data)) == data

data = "-1,0,1,None,None,None,None"
assert c.serialize(c.deserialize(data)) == data
