# LeetCode 36 - Valid Sudoku
# Difficulty: Medium
# Topic: Array, Hash Table, Matrix
# Time Complexity: O(1)
# Space Complexity: O(1)

class Solution(object):
    def isValidSudoku(self, board):
        
        for row in range(9):
            seen = set()
            for col in range(9):
                val = board[row][col]
                if val == ".":
                    continue
                if val in seen:
                    return False
                seen.add(val)

        for col in range(9):
            seen = set()
            for row in range(9):
                val = board[row][col]
                if val == ".":
                    continue
                if val in seen:
                    return False
                seen.add(val)

        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                seen = set()
                for i in range(3):
                    for j in range(3):
                        val = board[box_row + i][box_col + j]
                        if val == ".":
                            continue
                        if val in seen:
                            return False
                        seen.add(val)    
        
        return True                