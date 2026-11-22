from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        nums = defaultdict(list)
        row = 0
        col = 0
        while row < 9:
            while col < 9:
                print(row, col)
                if board[row][col] != ".":
                    square = [int(row / 3), int(col / 3)]
                    if nums[board[row][col]] != []:
                        for item in nums[board[row][col]]:
                            if row == item[0] or col == item[1] or square == item[2]:
                                return False    
                    nums[board[row][col]].append([row, col, square])
                col += 1
            row += 1
            col = 0
        return True