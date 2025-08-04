# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # create dummy node before the head, helps with edge case of head node being removed
        dummy = ListNode(0, head)
        # two pointers
        left = dummy
        right = head

        # keep moving right until n is 0, moving n times
        while n > 0:
            right = right.next
            n -= 1

        # now keep shifting until right hits the end of the list
        # this will now have the left node be at the position right before the node to remove
        while right:
            left = left.next
            right = right.next

        # remove target node, .next.next to get us the new pointer to the next node
        left.next = left.next.next
        # return the list starting from the original head
        return dummy.next