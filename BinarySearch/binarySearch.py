from typing import List

def search(nums: List[int], target: int) -> int:
    leftBound = 0
    rightBound = len(nums) - 1

    # keep searching while the window is valid (leftBound hasn't crossed rightBound)
    while leftBound <= rightBound:

        # calculate midpoint to avoid overflow (good practice, even if not needed in Python)
        midpoint = leftBound + ((rightBound - leftBound) // 2)

        # if the midpoint value is greater than the target, search the left half
        # we subtract 1 to exclude the midpoint since it's already checked
        if nums[midpoint] > target:
            rightBound = midpoint - 1

        # if the midpoint value is less than the target, search the right half
        # we add 1 to exclude the midpoint since it's already checked
        elif nums[midpoint] < target:
            leftBound = midpoint + 1

        # if it's equal, we've found the target
        else:
            return midpoint

    # target not found
    return -1
