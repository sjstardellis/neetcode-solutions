# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
from typing import Optional


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # default starting point, the current node is the head and the previous node is nothing
        prev = None
        curr = head

        # while current node is not null
        while curr:
            # save the next node for future reference
            nextNode = curr.next

            # set the next node as the previous to flip the pointer (first iteration will set the next pointer to null)
            curr.next = prev

            # set the previous pointer to the node as the current
            prev = curr

            # set the current node as the next node, restarting the process until we hit null
            curr = nextNode

        # returns the head of the new reversed list, in this case which is prev
        return prev


