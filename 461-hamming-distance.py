#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/hamming-distance/description/

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        
        return bin(x^y)[2:].count('1')

