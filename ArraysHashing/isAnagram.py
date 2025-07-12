def isAnagram(self, s: str, t: str) -> bool:
    # create two dictionaries to keep track the number of letters we got
    word1 = {}
    word2 = {}

    # loop through first word by character
    for char in s:
        # word1[char1] is identifying the character in the dictionary
        # add the char to the dictionary, default value is 0 if it doesn't exist or just add one if it does
        word1[char] = word1.get(char, 0) + 1
    # loop through second word by character
    for char in t:
        # add the char to the dictionary, default value is 0 if it doesn't exist or just add one if it does
        word2[char] = word2.get(char, 0) + 1

    # compare dictionaries to return a boolean
    return word1 == word2