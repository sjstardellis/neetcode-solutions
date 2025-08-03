class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # our fast and slow pointers
        slow, fast = 0, 0
        while True:
            # move one step
            slow = nums[slow]
            # move two steps
            fast = nums[nums[fast]]
            # break the while loop if they're equal
            if slow == fast:
                break
        # need to find the entry pointer of the cycle
        slow2 = 0 # starting at position 0, create a second slow pointer
        while True:
            # these will eventually intersect because slow and slow2 are the same distance at the start of the cycle
            # Floyd's Tortoise and Hare Algorithm property
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                # return the start the cycle, the duplicate
                return slow
