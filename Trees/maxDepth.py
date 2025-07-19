# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # initialize stack with root and depth of 1
        stack = [[root, 1]]

        # set maxDepth to 0 initially, that way that we can handle an empty tree case
        maxDepth = 0

        # DFS
        # as long as there are nodes to traversal, continue loop
        while stack:

            # take off the current node and depth from the stack
            node, depth = stack.pop()

            # only non-null nodes
            if node:
                # check to see if the current depth is greater than the max depth
                maxDepth = max(maxDepth, depth)
                # add children nodes onto the stack and update their depth
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        # return depth
        return maxDepth