#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ret = [0]
        for i in range(1, num+1):
            ret.append(ret[i>>1] + (i&1))
        return ret



solution = Solution()
assert solution.countBits(5) == [0,1,1,2,1,2]
        
