#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ERROR
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.inner(nums, 1, 1)

    def inner(self, nums, left, right):
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return left * right * nums[0]
        elif len(nums) == 2:
            if nums[0] < nums[1]:
                return left*nums[0]*nums[1] + left*nums[1]*right
            else:
                return nums[0]*nums[1]*right + left*nums[0]*right
        elif len(nums) == 3:
            products = []
            products.append(left*nums[0]*nums[1] + left*nums[1]*nums[2] + left*nums[2]*right)
            products.append(left*nums[0]*nums[1] + nums[1]*nums[2]*right + left*nums[1]*right)
            products.append(nums[0]*nums[1]*nums[2] + left*nums[0]*nums[2] + left*nums[2]*right)
            products.append(nums[0]*nums[1]*nums[2] + nums[0]*nums[2]*right + left*nums[0]*right)
            products.append(nums[0]*nums[1]*right + left*nums[0]*nums[2] + left*nums[2]*right)
            products.append(nums[0]*nums[1]*right + nums[0]*nums[2]*right + left*nums[0]*right)
            return max(products)

        sorted_indices = sorted(range(len(nums)), key=lambda k: nums[k])
        indices = sorted([sorted_indices[i] for i in (-1, -2, -3)])
        vals = [nums[i] for i in indices]

        ret = 0
        ret += self.inner(nums[:indices[0]], left, nums[indices[0]])
        ret += self.inner(nums[indices[0]+1:indices[1]], nums[indices[0]], nums[indices[1]])
        ret += self.inner(nums[indices[1]+1:indices[2]], nums[indices[1]], nums[indices[2]])
        ret += self.inner(nums[indices[2]+1:], nums[indices[2]], right)
        ret += self.inner(vals, 1, 1)
        return ret

# TLE
class Solution(object):
    def maxCoins(self, nums, cache = {}):
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]

        nums = tuple(nums)
        if nums in cache:
            return cache[nums]

        next_level = set()
        for i in range(0,len(nums)):
            val = nums[i]
            val *= nums[i-1] if i > 0 else 1 
            val *= nums[i+1] if i+1 < len(nums) else 1
            next_level.add((val, nums[:i]+nums[i+1:]))

        ret = 0
        for val, balloons in next_level:
            ret = max(ret, val + self.maxCoins(balloons, cache))
        cache[nums] = ret
        return ret

# solution = Solution()
# assert solution.maxCoins([3,1,5,8]) == 167
# assert solution.maxCoins([9,76,64,21]) == 116718
# assert solution.maxCoins([35,16,83,87,84,59,48,41,20,54]) == 1849648
# assert solution.maxCoins([8,2,6,8,9,8,1,4,1,5,3,0,7,7,0,4,2]) == 3414

# dp[i][j] means the maximum coin we can get if we keep the i,j balloons and burst only the
# [i+1..j-1] balloons.
class Solution(object):
    def maxCoins(self, nums):
        if not nums:
            return 0

        dp = {}
        nums = [1] + nums + [1]
        for gap in range(1, len(nums)):
            for i in range(0, len(nums)-gap):
                j = i + gap
                vals = [dp.get((i, k)) + dp.get((k, j)) + nums[i]*nums[j]*nums[k] for k in range(i+1, j)]
                vals.append(0)
                dp[(i, j)] = max(vals)

        return dp[(0, len(nums)-1)]

solution = Solution()
assert solution.maxCoins([3,1,5,8]) == 167
assert solution.maxCoins([9,76,64,21]) == 116718
assert solution.maxCoins([35,16,83,87,84,59,48,41,20,54]) == 1849648
assert solution.maxCoins([8,2,6,8,9,8,1,4,1,5,3,0,7,7,0,4,2]) == 3414
