#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

        if p == "":
            return []

        ret = []

        l = len(p)

        subset = [0] * 128
        target = [0] * 128
        for c in s[:l-1]:
            subset[ord(c)] += 1
        for c in p:
            target[ord(c)] += 1

        for i in range(len(s)-l+1):
            subset[ord(s[i+l-1])] += 1

            if subset == target:
                ret.append(i)

            subset[ord(s[i])] -= 1

        return ret
            
solution = Solution()
assert solution.findAnagrams("cbaebabacd", "abc") == [0, 6]
assert solution.findAnagrams("abab", "ab") == [0, 1, 2]
