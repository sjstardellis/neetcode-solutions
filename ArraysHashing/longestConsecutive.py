from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # our unique list of numbers, already set from nums
        seen = set(nums)
        # keep track of the longest consecutive number string
        longest = 0

        # looping through the set
        for num in seen:
            # if the number before the current number is not in seen, start the sequence
            if (num - 1) not in seen:
                # set the length to 1
                length = 1
                # while the length + current number is in seen
                # will activate when the lowest number is seen
                while (num+length) in seen:
                    # keep adding to the length
                    length += 1
                # compare current length to the longest length, set the variable to the bigger number
                longest = max(length, longest)
        return longest