class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_list = defaultdict(list)
        column_list = defaultdict(list)
        square_list = defaultdict(list)

        for row in range(len(board)):
            for column in range(len(board)):
                value = board[row][column]

                if value == '.':
                    continue

                if value in row_list[row] or value in column_list[column] or value in square_list[(row//3,column//3)]:
                    return False
                else:
                    row_list[row].append(value)
                    column_list[column].append(value)
                    square_list[(row//3,column//3)].append(value)

        return True