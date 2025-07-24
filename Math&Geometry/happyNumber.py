class Solution:
    def isHappy(self, n: int) -> bool:
        # initializing our values, comparing them to detect a cycle
        # eventually fast will lap slow if there is a cycle
        # cannot do both slow and fast as n because then we can't detect a cycle
        slow, fast = n, self.sumOfSquares(n)

        # continue while loop unless there is a cycle (meaning the number has been seen)
        while slow != fast:
            # do two sum of squares
            fast = self.sumOfSquares(fast)
            fast = self.sumOfSquares(fast)
            # do one
            slow = self.sumOfSquares(slow)

        # if it is a happy number, it will continuously repeat 1^2, otherwise it will not be a happy number
        return True if fast == 1 else False

    # sum up the digits and square them
    def sumOfSquares(self, n: int) -> int:
        output = 0
        # while not null
        while n:
            # get the last digit
            digit = n % 10
            # square it
            digit = digit ** 2
            # running sum
            output += digit
            # remove the last digit
            n = n // 10
        return output
        # not the most space efficient solution
        # seen = set()
        # total = n
        #
        # while total:
        #     sum_squares = sum([int(d) ** 2 for d in str(total)])
        #     if sum_squares == 1:
        #         return True
        #     if sum_squares not in seen:
        #         seen.add(sum_squares)
        #     else:
        #         return False
        #     total = sum_squares