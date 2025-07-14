from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        # store the final result, where result[i] = product of all nums except nums[i]
        resultArray = [1] * n

        # calculate prefix product for each index.
        # stores the product of all elements to the left of the current index.
        prefix = 1
        for i in range(n):
            # set the current index in resultArray to the prefix product, default is 1
            resultArray[i] = prefix

            # update prefix to include nums[i] for the next iteration
            prefix = prefix * nums[i]

        # calculate suffix product for each index
        # stores the product of all elements to the right of the current index

        suffix = 1
        # iterate backwards through nums array
        for i in range(n - 1, -1, -1):
            # starting backwards, updating the resulting array by multiplying current value by suffix
            resultArray[i] = resultArray[i] * suffix

            # update suffix by multiplying the original array's value at the location
            suffix = suffix * nums[i]

        return resultArray
