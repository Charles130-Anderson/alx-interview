#!/usr/bin/python3
"""
Defines function to calculate
minimum number of coins needed.
"""


def makeChange(coins, total):
    """
    Calculate fewest number coins.
    Args:
        coins (list): List of coin
        denominations.
        total (int): Target amount to
        achieve.
    Returns:
        int: Fewest coins needed for
        given total, or -1 if not
        possible.
    """
    if total <= 0:
        return 0
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[total] if dp[total] != float('inf') else -1


if __name__ == "__main__":
    """
    Main test cases for function.
    """
    print(makeChange([1, 2, 25], 37))  # Expected output: 7
    print(makeChange([1256, 54, 48, 16, 102], 1453))  # Expected output: -1
