class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_list = defaultdict(set)
        column_list = defaultdict(set)
        square = defaultdict(set)

        for row in range(len(board)):
            for column in range(len(board)):

                value = board[row][column]

                if value == ".":
                    continue

                if value in row_list[row] or value in column_list[column] or value in square[(row//3,column//3)]:
                    return False

                row_list[row].add(value)
                column_list[column].add(value)
                square[(row//3,column//3)].add(value)

        return True