# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # create a dummy node, the head of the new list is -1
        current = dummy = ListNode(-1)


        # while both lists are not null
        while list1 and list2:
            # if the list1 current node is less than the list2 current node, add the list1 node to the new list
            if list1.val < list2.val:
                current.next = list1
                # move the node pointer on list1
                list1 = list1.next
            # if the list2 current node is less than the list1 current node, add the list2 node to the new list
            else:
                current.next = list2
                # move the node pointer on list2
                list2 = list2.next
            current = current.next

        # add the rest of the list if they are not the same size
        current.next = list1 if list1 else list2

        # starts at the actual head, since the head at just dummy is -1
        return dummy.next