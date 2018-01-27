#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.trie
        for c in word:
            child = node.get(c, {})
            node[c] = child
            node = child
        node["word"] = word

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """

        node = self.trie
        for c in word:
            node = node.get(c, None)
            if node is None:
                return False

        return "word" in node;

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """

        node = self.trie
        for c in prefix:
            node = node.get(c, None)
            if node is None:
                return False
        return True

trie = Trie()
trie.insert("to")
trie.insert("tea")
trie.insert("ted")
trie.insert("ten")
trie.insert("inn")
