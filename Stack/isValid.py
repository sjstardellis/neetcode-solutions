class Solution:
    def isValid(self, s: str) -> bool:

        # stack keeps track of open brackets, if it is empty then it is valid
        stack = []

        # dictionary of valid parenthesis pattern
        closeToOpen = {")": "(",
                       "]": "[",
                       "}": "{"}

        # going through all the characters in the string
        for c in s:
            # is the current character a closing bracket
            if c in closeToOpen:
                # make sure stack isn't empty
                # value at the top of the stack (last value) is the matching parenthesis

                # and also if it equals to the corresponding opening brace
                if stack and stack[-1] == closeToOpen[c]:
                    # remove that last value of the stack
                    stack.pop()
                else:
                    # if stack is empty or parenthesis doesn't match order
                    return False
            else:
                # add to stack for open parenthesis
                stack.append(c)
        # returns true if stack is empty
        return not stack
