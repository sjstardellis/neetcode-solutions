class Solution:
    
    def encode(self, strs: List[str]) -> str:
        # resulting string is empty
        res = ""

        # go string by string
        for s in strs:
            # take the current result, adding length of the current string + '#' + the actual string itself
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        # resulting list of strings
        res = []
        # tracks the beginning of the string
        i = 0
        # loop while there are characters left in the encoded string
        while i < len(s):
            # j is the end boundary of the current string
            j = i
            # while the current pointer is not at the '#'
            while s[j] != '#':
                # keep moving until we find the pound
                j += 1
            # once we get to '#', gives us the length of the string based on the array slice
            length = int(s[i:j])
            # j is at the delimiter, j+1 will get to the first character of the string
            i = j + 1
            # go until the end of the string, which is the first character to the last character (based on length value)
            j = i + length
            # extract the substring and append it to the result list
            res.append(s[i:j])
            # setting the new starting point to be at the last chacter
            i = j
        return res
