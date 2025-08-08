from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # define lengths of matrix
        ROWS, COLS = len(matrix), len(matrix[0])
        # marker for whether the first row needs to be zeroed
        rowZero = False

        # looping through all the rows
        for r in range(ROWS):
            # each column of every row
            for c in range(COLS):
                # if the number is 0
                if matrix[r][c] == 0:
                    # mark the first cell in the column (0th row) as 0
                    matrix[0][c] = 0
                    # if not in the 0th row, mark the first element in the row as 0
                    if r > 0:
                        matrix[r][0] = 0
                    # special case: if the 0 is in the first row, use rowZero instead of matrix[0][0]
                    else:
                        rowZero = True

        # zero cells based on markers, excluding row 0 and column 0
        for r in range(1, ROWS):
            for c in range(1, COLS):
                # if there is a marker at the beginning of the row or column, mark the current index as 0
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # if [0][0] is 0, then make the first column all zeroes
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0

        # if rowZero is true (meaning 0 was found in the first row)
        if rowZero:
            # zero out the first row
            for c in range(COLS):
                matrix[0][c] = 0
