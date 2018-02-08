#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Counter

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """

        counter = Counter(tasks).most_common()
        count_of_most_common = counter[0][1]
        num_of_most_elements = len([x for x in counter if x[1] == count_of_most_common])

        least = count_of_most_common + (count_of_most_common-1)*n + num_of_most_elements - 1

        return max(least, len(tasks))
        
solution = Solution()
assert solution.leastInterval(["A","A","A","B","B","B"], 2) == 8
assert solution.leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2) == 16
