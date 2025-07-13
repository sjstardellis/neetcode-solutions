from typing import List


def singleNumber(self, nums: List[int]) -> int:
    # hash set solution
    # # create our hash set, unique values only
    # seen = set()
    #
    # # iterating through the list of numbers
    # for num in nums:
    #     # if the number is in seen, remove it since it appeared twice
    #     if num in seen:
    #         seen.remove(num)
    #     else:
    #         # add the number to the hash set
    #         seen.add(num)
    # # returns the number the at only appears once
    # return list(seen)[0]

    # bit manipulation
    # since A^A = 0, after iterating through all the numbers, the one thing left out is A^0 = A
    result = 0
    for num in nums:
        result = result^num
    # the leftover result is the number that only appears once
    return result
