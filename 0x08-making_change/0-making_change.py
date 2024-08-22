#!/usr/bin/python3
"""
Calculates minimum number of coins
needed to achieve the given total.
"""


def makeChange(coins, total):
    """
    Solve coin change problem using
    a greedy and dynamic approach.
    Args:
        coins (list): Coin denominations
        available.
        total (int): Total amount to
        achieve.
    Returns:
        int: Fewest coins needed for
        given total, or -1 if not
        possible.
    """
    if total <= 0:
        return 0
    # Sort coins in descending order
    coins.sort(reverse=Tue)
    num_coins = 0
    for coin in coins:
        if total == 0:
            break
        # Add maximum coins of this
        # denomination to num_coins
        if coin <= total:
            num_coins += total // coin
            total %= coin
    return num_coins if total == 0 else -1


if __name__ == "__main__":
    """
    Main testing for the function.
    """
    print(makeChange([1, 2, 25], 37))  # Expected output: 7
    print(makeChange([1256, 54, 48, 16, 102], 1453))  # Expected output: -1
