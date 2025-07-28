class Solution:
    def countBits(self, n: int) -> List[int]:
        # creates a list of 0s length of n+1
        dp = [0] * (n + 1)

        # tracks most recent power of 2
        offset = 1

        # looping through every number 1-(n+1) include
        for i in range(1, n + 1):
            # if the i is double fo the current offset
            if offset * 2 == i:
                # set the new offset to i
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp