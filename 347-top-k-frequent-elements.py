#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = defaultdict(lambda: 0)
        for num in nums:
            counts[num] += 1

        count_num_mapping = [set() for _ in range(len(nums)+1)]
        for num, count in counts.items():
            count_num_mapping[count].add(num)

        ret = []
        count = len(nums)
        while count >= 0 and len(ret) < k:
            while count >= 0 and len(count_num_mapping[count]) == 0:
                count -= 1
            ret.append(count_num_mapping[count].pop())
        return ret

solution = Solution()
assert solution.topKFrequent([1,1,1,2,2,3], 2) == [1,2]
assert solution.topKFrequent([1], 1) == [1]
assert solution.topKFrequent([1,2], 2) == [1,2]
