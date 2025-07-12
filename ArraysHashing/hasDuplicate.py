from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # creates hash set, can't have duplicates since it's a set
        seen = set()

        # loop through the array of integers nums
        for i in nums:
            # if the current number is in the seen set
            if i in seen:
                # return true
                return True
            # if not true, add this number to the set
            seen.add(i)
        # if loop finishes, then return false
        return False