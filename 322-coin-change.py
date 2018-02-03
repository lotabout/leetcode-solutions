#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# WRONG ANSWER
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        return self.inner(list(reversed(sorted(coins))), amount)

    def inner(self, coins, amount):
        if not coins or amount < 0:
            return -1

        coin = coins[0]
        num = amount // coin
        if amount % coin == 0:
            return num

        for i in range(num, -1, -1):
            rest = amount - i*coin
            num_rest = self.inner(coins[1:], rest)
            if num_rest >= 0:
                return i + num_rest

        return -1

# BFS, TLE
class Solution(object):
    def coinChange(self, coins, amount):
        return self.inner(set(coins), set([amount]), 0)

    def inner(self, coins, amounts, count):
        if not amounts:
            return -1

        if 0 in amounts:
            return count

        next_round = set()
        for amount in amounts:
            for coin in coins:
                if amount == coin:
                    return count + 1
                if amount > coin:
                    next_round.add(amount - coin)
        return self.inner(coins, next_round, count+1)

# DFS + cache
from collections import defaultdict
class Solution(object):
    def coinChange(self, coins, amount):
        dp = {0: 0}
        for coin in coins:
            dp[coin] = 1
        return self.inner(coins, amount, dp)

    def inner(self, coins, amount, dp):
        if amount in dp:
            return dp[amount]
        elif amount < 0:
            return -1

        num = -1
        for coin in coins:
            if amount >= coin:
                next_round = self.inner(coins, amount-coin, dp)+1
                if next_round > 0 and (num == -1 or num > next_round):
                    num = next_round

        dp[amount] = num
        return dp[amount]

# Pure DP
class Solution(object):
    def coinChange(self, coins, amount):
        MAX = float('inf')
        dp = [0] + [MAX] * amount
        for i in range(1, amount+1):
            for coin in coins:
                if i == coin:
                    dp[i] = 1
                elif i > coin:
                    if dp[i-coin]+1 < dp[i]:
                        dp[i] = dp[i-coin]+1
        return -1 if dp[amount] == MAX else dp[amount]

solution = Solution()
assert solution.coinChange([1,2,5], 11) == 3
assert solution.coinChange([1], 0) == 0
assert solution.coinChange([2], 1) == -1
assert solution.coinChange([2], 3) == -1
assert solution.coinChange([186,419,83,408], 6249) == 20
assert solution.coinChange([125,146,125,252,226,25,24,308,50], 8402) == 29
