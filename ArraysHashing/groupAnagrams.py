from collections import defaultdict
from typing import List


def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    # key is the letters of a word
    # value is the words that have the same number of letters and same letters

    # defaultdict automatically creates a key entry if it doesn't exist
    results = defaultdict(list)

    # looping through each word in the list o fstrings
    for word in strs:
        # 26 0s, one for each character from a-z
        count = [0] * 26

        # going through every character of each word
        for char in word:
            # index 0-25 will be mapped to a-z
            # using ASCII values, we can find which letter we are at by doing
            # for example a - a should equal 0, b - a should be 1, and so on
            # += for each character seen
            count[ord(char) - ord('a')] += 1
        # add the word to the list of words for the key value of the count array
        # essentially for each group of letters case, add the word that maches is.

        # tuple makes it immutable
        results[tuple(count)].append(word)

    # return the groups of the values
    return list(results.values())
