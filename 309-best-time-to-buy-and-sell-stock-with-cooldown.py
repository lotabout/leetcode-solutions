#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# TLE
# buy(x) = max(sell(x+1, price[x]), buy(x+1))
# sell(x, val) = max(prices[x]-val+buy(x+2), sell(x+1, val))
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        return self.buy(prices, 0, {}, {})

    def buy(self, prices, x, cache_buy = {}, cache_sell = {}):
        if x in cache_buy:
            return cache_buy[x]

        if x + 1 >= len(prices):
            ret = 0
        else:
            ret = max(self.sell(prices, x+1, prices[x], cache_buy, cache_sell),
                    self.buy(prices, x+1, cache_buy, cache_sell))
        cache_buy[x] = ret
        return ret

    def sell(self, prices, x, val, cache_buy = {}, cache_sell = {}):
        if (x, val) in cache_sell:
            return cache_sell[(x, val)]

        if x == len(prices) - 1:
            ret = max(0, prices[x] - val)
        else:
            ret = max(prices[x]-val + self.buy(prices, x+2, cache_buy, cache_sell),
                    self.sell(prices, x+1, val, cache_buy, cache_sell))
        cache_sell[(x, val)] = ret
        return ret


# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/discuss/75927/
# b[i] means the max profit of prices[:i+1] that ends on buy
#
# b[i] = sell_rest[i-1] - price
# s[i] = max(b[i-1], buy_rest[i-1]) + price
# sell_rest[i] = max(s[i-1], sell_rest[i])
# buy_rest[i] = max(b[i-1], buy_rest[i])

# learnt to treat problems as mathmatical equations (recursion)

class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0

        buy, sell, sell_rest, buy_rest = -prices[0], 0, 0, -sum(prices) 
        for p in prices:
            nbuy = sell_rest - p
            nsell = max(buy, buy_rest) + p
            nsell_rest = max(sell, sell_rest)
            nbuy_rest = max(buy, buy_rest)
            buy, sell, sell_rest, buy_rest = nbuy, nsell, nsell_rest, nbuy_rest
        return max([buy, sell, sell_rest, buy_rest])

solution = Solution()
assert solution.maxProfit([]) == 0
assert solution.maxProfit([1, 2, 3, 0, 2]) == 3
