# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # two pointers, one iterating by +1 and another by +2
        slow, fast = head, head

        # while both are not null
        while fast and fast.next:
            # go +1
            slow = slow.next
            # go +2
            fast = fast.next.next
            # if the fast one ever catches up to and loops around, then return true
            if slow == fast:
                return True
        # return false
        return False