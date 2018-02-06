#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# O(n^2) but could achieve O(n lg n) if using binary indexed tree
class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """

        ret = [None] * len(people)

        for h, k in sorted(people):
            k_back = k
            idx = -1 
            for x in ret:
                if x is None or x[0] == h:
                    idx += 1
                    k -= 1
                else:
                    idx += 1

                if x is None and k < 0:
                    ret[idx] = [h, k_back]
                    break
        return ret

solution = Solution()
assert solution.reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]) == [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
assert solution.reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]) == [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
