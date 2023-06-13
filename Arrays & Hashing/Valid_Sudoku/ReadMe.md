# Valid Sudoku

### Determine if a 9 x 9 Sudoku board is valid.
```
# Time complexity: O(n^2) 
# O(n)
class Solution(object):
    def isValidSudoku(self, board):
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        #iterate grid
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if (board[row][col] in rows[row] or board[row][col] in cols[col] or board[row][col] in squares[(row // 3, col // 3)]):
                    return False
                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                squares[(row//3, col//3)].add(board[row][col])
        return True
```

### Solution description:
### We initialize 3 hashsets, iterate through the board, and add the number to each hashset (each hashset has a different vision of the board). Also, before adding the number to the hashsets, we verify if it is not already present in one of them. If that is the case, return False.