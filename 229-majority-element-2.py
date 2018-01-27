#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/majority-element-ii/

# I finished majorityElement-I with O(1) space but cannot solve this one.
# Like different armies want to take over 2 positions
# There are armies whose number is greater than floor of n/3. Thus if each soldier can take down one
# soldier on the position, the army will survive after fight with all others.
# But since the number is not majority(> n/2), they could fight with at most the other n/3 soldiers.
# so the following code is important to avoid fights.
#
#  elif n1 == 0:
#     candidate1, n1 = n, 1
#  elif n2 == 0:
#     candidate2, n2 = n, 1
#
# If there is an empty position, the solider will take over the position directly without fighting
# the other positions.

class Solution:
    def majorityElement(self, nums):
        if len(nums) == 0:
            return []

        candidate1, n1 = None, 0
        candidate2, n2 = None, 0

        for n in nums:
            if n == candidate1:
                n1 += 1
            elif n == candidate2:
                n2 += 1
            elif n1 == 0:
                candidate1, n1 = n, 1
            elif n2 == 0:
                candidate2, n2 = n, 1
            else:
                n1 -= 1
                n2 -= 1
        return [x for x in (candidate1, candidate2) if nums.counts(x) > len(nums)//3]
