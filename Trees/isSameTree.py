# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # used for traversal, at the root nodes of both q and p
        stack = [[p, q]]

        # as long as there are nodes for traversal, continue loop
        while stack:
            # take off the top pair of nodes of the stack
            node1, node2 = stack.pop()

            # if they are not both null, continue
            if not node1 and not node2:
                continue

            # if one of them is none/null or if not the same value, return false
            if not node1 or not node2 or node1.val != node2.val:
                return False

            # add children to the stack
            stack.append((node1.right, node2.right))
            stack.append((node1.left, node2.left))
        return True
