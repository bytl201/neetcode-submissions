class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        seen = set()
        rows = len(board)
        columns = len(board[0])

        def dfs(index, row, column):
            if index == len(word):
                return True
            if row < 0 or column < 0 or column >= columns or row >= rows or word[index] != board[row][column] or (row, column) in seen:
                return False
            seen.add((row, column))

            if dfs(index +1, row+1, column) or dfs(index+1, row, column+1) or dfs(index+1, row-1, column) or dfs(index+1, row, column-1):
                return True

            seen.remove((row, column))
            return False

        
        for row in range(rows):
            for column in range(columns):
                if dfs(0, row, column):
                    return True

        return False
