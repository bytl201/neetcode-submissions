class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_list = defaultdict(list)
        column_list = defaultdict(list)
        square_list = defaultdict(list)

        for row in range(len(board)):
            for column in range(len(board)):
                num = board[row][column]

                if num == ".":
                    continue
                
                if num in row_list[row] or num in column_list[column] or num in square_list[(row//3,column//3)]:
                    return False
                
                row_list[row].append(num)
                column_list[column].append(num)
                square_list[(row//3,column//3)].append(num)
        return True
                