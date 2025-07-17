class Solution:
    def isPalindrome(self, s: str) -> bool:

        # left and right pointer starting pointers
        pointer1, pointer2 = 0, len(s) - 1

        # while the pointers have not crossed
        while pointer1 < pointer2:
            # if character is not alphanumeric, move left pointer forward
            while pointer1 < pointer2 and not self.alphaNum(s[pointer1]):
                pointer1 += 1

            # if character is not alphanumeric, move right pointer backward
            while pointer2 > pointer1 and not self.alphaNum(s[pointer2]):
                pointer2 -= 1

            # if the characters we're comparing are not the same, then return false
            if s[pointer1].lower() != s[pointer2].lower():
                return False

            # otherwise, update pointers to close in one position
            pointer1, pointer2 = pointer1 + 1, pointer2 - 1

        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
