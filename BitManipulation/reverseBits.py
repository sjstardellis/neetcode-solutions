class Solution:
    def reverseBits(self, n: int) -> int:
        # store our result
        res = 0

        # loop through each digit
        for i in range(32):
            # since AND 1 only works on the first bit on the right side, we must shift n by i times
            # right to left
            bit = (n >> i) & 1

            # starting from left to right now, shifting to that position
            # res uses OR (|) to set bits: if res currently has 0 at that position, and bit is 1,
            # OR will set that bit to 1; if bit is 0, OR keeps the existing bit in res unchanged.
            res = res | (bit << (31 - i))
        return res