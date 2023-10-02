# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
from typing import List


def maxProfit(prices: List[int]) -> int:
    """
    Calculate the timestamps for the best price to buy and sell the stock resulting in the maximum profit.
    :param prices: list of prices for the stock
    :return: maximum profit
    :rtype: int
    """
    min_price_ind = cur_min_ind = 0
    max_price_ind = 1

    # if there is only one price, there is no profit
    if len(prices) < 2:
        return 0

    for ind in range(1, len(prices)):
        # if the current price is lower than the current minimum, update the current minimum
        if prices[ind] < prices[cur_min_ind]:
            cur_min_ind = ind

        # if the difference between the current price and the current minimum is greater than the difference between the maximum price and the minimum price, update the maximum and minimum prices
        if prices[ind] - prices[cur_min_ind] > prices[max_price_ind] - prices[min_price_ind]:
            min_price_ind = cur_min_ind
            max_price_ind = ind

    res = prices[max_price_ind] - prices[min_price_ind]
    return res if res > 0 else 0
