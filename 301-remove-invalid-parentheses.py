#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/remove-invalid-parentheses/description/

# BFS
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        if self.is_valid(s):
            return [s]

        return self.removeOneParentheses([s])
        
    def removeOneParentheses(self, candidates):
        if not candidates:
            return []

        new_candidates = set()

        for candidate in candidates:
            for i in range(len(candidate)):
                new_candidates.add(candidate[:i] + candidate[i+1:])

        ret = list(filter(self.is_valid, new_candidates))
        if len(ret) > 0:
            return ret
        else:
            return self.removeOneParentheses(new_candidates)

    def is_valid(self, s):
        stack = 0
        for c in s:
            if c == '(':
                stack += 1
            elif c == ')':
                stack -= 1
            if stack < 0:
                return False
        return stack == 0

solution = Solution()
assert set(solution.removeInvalidParentheses("()())()")) == set(["()()()", "(())()"])
assert set(solution.removeInvalidParentheses("(a)())()")) == set(["(a)()()", "(a())()"])
assert solution.removeInvalidParentheses(")(") == [""]
assert solution.removeInvalidParentheses("") == [""]
