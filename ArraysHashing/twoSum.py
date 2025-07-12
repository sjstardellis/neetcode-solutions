from typing import List


def twoSum(self, nums: List[int], target: int) -> List[int]:
    # create hash map to store previously seen numbers
    # key is the number, the value is the index in the list
    prevMap = {}  # val -> index

    # loop through the list of numbers, getting both index and value
    # enumerate allows us to get the index and the value at the same time
    for currentIndex, currentNum in enumerate(nums):

        # calculating the difference from the target minus the current number
        diff = target - currentNum

        # if the difference is in the hashmap, return the indexes
        if diff in prevMap:
            return [prevMap[diff], currentIndex]

        # if not, add the current number and index to the hashmap
        prevMap[currentNum] = currentIndex