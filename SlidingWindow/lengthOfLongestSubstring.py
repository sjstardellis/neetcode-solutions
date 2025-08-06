class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        longest = 0
        start = 0

        for i, char in enumerate(s):
            # if the character is already seen AND
            # if last index where char was found is >= the current index
            if char in seen and seen[char] >= start:
                # move window start just after duplicate
                start = seen[char] + 1
            # update last seen index
            seen[char] = i
            # length of current window
            longest = max(longest, i - start + 1)

        return longest