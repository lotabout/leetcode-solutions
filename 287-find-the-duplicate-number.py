#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/find-the-duplicate-number/description/

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        bit_arrays = [self.to_bit_array(num) for num in range(len(nums))]
        expected_bits = map(lambda *x: sum(x), *bit_arrays)

        bits = map(lambda *x: sum(x), *[self.to_bit_array(num) for num in nums])

        ret_bits = map(lambda r, e: 1 if r > e else 0, bits, expected_bits)
        return sum([ret_bits[i] << i for i in range(32)])

    def to_bit_array(self, num):
        return [num >> i & 1 for i in range(32)]
