from collections import defaultdict
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # defaultdict automatically creates a key entry if it doesn't exist
        # initializing our seen numbers
        columns_seen = defaultdict(set)
        rows_seen = defaultdict(set)
        squares_seen = defaultdict(set)

        # over each slot on the board
        for row in range(9):
            for col in range(9):
                # if the slot is a ".", move to the next slot
                if board[row][col] == ".":
                    continue
                if(
                    board[row][col] in rows_seen[row] or
                    board[row][col] in columns_seen[col] or
                    # row // 3, col // 3 helps identify which square the slot is in
                    board[row][col] in squares_seen[(row // 3, col // 3)]):
                    return False
                # if not in any of the squares, rows, or columns, then add the number into the entry
                # now if the same number
                columns_seen[col].add(board[row][col])
                rows_seen[row].add(board[row][col])
                squares_seen[(row // 3, col // 3)].add(board[row][col])
        # if it exits the loop, then true
        return True



