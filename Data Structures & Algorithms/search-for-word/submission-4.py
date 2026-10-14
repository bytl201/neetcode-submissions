class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        seen = set()
        rows = len(board)
        columns = len(board[0])


        def dfs(row, column, index):
            if index == len(word):
                return True

            if row < 0 or row >= rows or column < 0 or column >= columns or word[index] != board[row][column] or (row,column) in seen:
                return False
            
            seen.add((row,column))
            if dfs(row-1, column, index+1) or dfs(row, column-1, index+1) or dfs(row+1, column, index+1) or dfs(row, column+1, index+1):
                return True
            
            seen.remove((row,column))
            
            return False
            

        for row in range(rows):
            for column in range(columns):
                if dfs(row, column, 0):
                    return True
        return False

