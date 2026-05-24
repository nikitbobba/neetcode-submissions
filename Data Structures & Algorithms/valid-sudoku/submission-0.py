from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                val = board[r][c]
                print(val, rows, cols, squares)
                if val not in rows[r] and val not in cols[c] and val not in squares[(int(r/3), int(c/3))]:
                    # valid point add it to all the sets
                    rows[r].add(val)
                    cols[c].add(val)
                    squares[(int(r/3), int(c/3))].add(val)
                else:
                    return False
        
        return True


        