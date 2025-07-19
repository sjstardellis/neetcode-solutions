from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        # length of the list
        n = len(digits)
        # looping from n-1 to 0
        for i in range(n - 1, -1, -1):
            # if the current digit is less than 9, just simply add 1 and return list
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # if not, then set that current number at that index to 0, continue with loop
            digits[i] = 0
        # if all the numbers in the array are 0, then it will reach this block and add 1 in the front
        return [1] + digits