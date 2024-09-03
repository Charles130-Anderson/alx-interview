#!/usr/bin/python3

def sieve_of_eratosthenes(max_n):
    """Generate a list of primes up to max_n
    using the Sieve of Eratosthenes."""
    is_prime = [True] * (max_n + 1)
    p = 2
    while p * p <= max_n:
        if is_prime[p]:
            for i in range(p * p, max_n + 1, p):
                is_prime[i] = False
        p += 1
    return [p for p in range(2, max_n + 1) if is_prime[p]]


def isWinner(x, nums):
    """Determine the player who wins the most rounds."""
    if not nums:
        return None

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n < 2:
            ben_wins += 1
            continue

        # Initialize game state
        numbers = [True] * (n + 1)
        turn = 0  # 0 for Maria, 1 for Ben
        for prime in primes:
            if prime > n:
                break
            if numbers[prime]:
                # Remove prime and its multiples
                for multiple in range(prime, n + 1, prime):
                    numbers[multiple] = False
                # Switch turn
                turn = 1 - turn

        # Determine the winner of this round
        if turn == 0:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
