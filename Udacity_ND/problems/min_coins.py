def coinChange(coins: List[int], amount: int) -> int:
    """
    Function to find the minimum number of coins needed to make the given amount.

    Parameters:
    - coins: List of integers, represents different coin denominations.
    - amount: Integer, the target amount.

    Returns:
    - Integer, representing the minimum number of coins. Returns -1 if not possible.
    """
    # Initialize a DP array with length `amount + 1` and set it to a large number
    # DP[amount] will contain the minimum number of coins needed for amount `amount`
    dp = [float('inf')] * (amount + 1)

    # Base case: Minimum coins needed for amount 0 is 0
    dp[0] = 0

    # Loop through all amounts from 1 to `amount`
    for amount in range(1, amount + 1):
        for coin in coins:
            # Update DP value if it's possible to make the amount using the current coin
            if amount - coin >= 0:
                # min coins for amount `amount` = min of (current min coins for amount `amount`, min coins for amount `amount - coin` + 1)
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # Return the answer or -1 if not possible
    return dp[amount] if dp[amount] != float('inf') else -1
