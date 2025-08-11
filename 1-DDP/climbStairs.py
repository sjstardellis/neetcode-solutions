class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        # storing our results from 0 to n
        dp = [0] * (n + 1)
        # initialize our default values (base case)
        dp[1], dp[2] = 1, 2
        # now from 3 to n+1
        for i in range(3, n + 1):
            # number of ways to reach step i is the sum of:
            # - ways to reach step (i-1) and then take 1 step
            # - ways to reach step (i-2) and then take 2 steps
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]