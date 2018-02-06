#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        chars = [c for c in reversed(s)]
        return self.parse(chars)

    def parse(self, chars):
        ret = []
        while chars and chars[-1] != ']':
            ret.append(self.rec(chars))
        return "".join(ret)

    def rec(self, chars):
        if not chars:
            return ""
        elif '0' <= chars[-1] <= '9':
            num = 0
            while '0' <= chars[-1] <= '9':
                num = num * 10 + int(chars.pop())
            chars.pop() # '['
            ret = self.parse(chars)
            chars.pop() #']'
            return ret * num
        elif chars[-1] == ']':
            return
        else:
            # valid chars
            return chars.pop()

solution = Solution()
assert solution.decodeString("3[a]2[bc]") == "aaabcbc"
assert solution.decodeString("3[a2[c]]") == "accaccacc"
assert solution.decodeString("2[abc]3[cd]ef") == "abcabccdcdcdef"
