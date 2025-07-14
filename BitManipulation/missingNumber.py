from typing import List


def missingNumber(self, nums: List[int]) -> int:

    # # brute force solution
    # count = 0
    # for n in nums:
    #     if n != count:
    #         return count
    #     count += 1

    # proper solution
    # getting the size of the array,
    res = len(nums)

    # range allows it to go from 0 to n-1
    # sum of expected indices − sum of actual values = missing number
    for i in range(len(nums)):
        # essentially (i - nums[i]) should be 0, unless the missing number shows up
        # if the missing number shows up, we get the complement of it
        # i is the index and nums[i] should be the number its storing
        res = res + (i - nums[i])
    # return missing number
    return res
