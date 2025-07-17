from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0 # left pointer
        sell = 1 # right pointer

        currentMax = 0

        # while the left pointer hasn't gone all the way through
        while sell < len(prices):
            # check to see if there is a dip
            if prices[buy] < prices[sell]:
                # is the new profit greater than the current max
                if currentMax < prices[sell]-prices[buy]:
                    # set current max
                    currentMax = prices[sell]-prices[buy]

            else:
                # set buy to current sell position
                buy = sell
            # move sell forward to seek out more profit
            sell = sell + 1
        return currentMax


