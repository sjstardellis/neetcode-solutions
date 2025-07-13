from typing import List


def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    # our hashmap to store our frequencies
    # key -> the frequency of that number
    # value -> the numbers that satisfy this

    count = {}

    # index is going to be the frequency and the value is the list of numbers that satisfy this
    # + 1 for 0 slot
    frequency = [[] for i in range(len(nums) + 1)]

    for n in nums:
        # initializing all our numbers in the hashmap
        count[n] = count.get(n, 0) + 1

    # using .items(), first variable maps to the key and the second variable maps to the value, conveniently named here
    # builds our frequency buckets in our array
    for key, value in count.items():
        # key and value switch in the array
        # index of the array represents the number of times a number shows up
        # the numbers in the array at the specific index are the ones that satisfy that requirement
        frequency[value].append(key)

    # our results array to store our top k elements
    result = []

    # start from descending order to get the top k elements
    # start from the largest values right edge case and go all the way to 0, subtracting 1 each time
    for i in range(len(frequency) - 1, 0, -1):
        # going through all the numbers in each array of each index
        for number in frequency[i]:
            # cannot be top 0 elements, so there must always be 1
            # append the number to results array
            result.append(number)
            # check to see if we have reached k elements, if so return the array
            if len(result) == k:
                return result