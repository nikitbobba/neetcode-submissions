class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        topLeft = matrix[0][0]

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    # update the row pointer
                    matrix[0][col] = 0

                    if row > 0:
                        matrix[row][0] = 0
                    else:
                        topLeft = 0
                else:
                    continue
        

        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        
        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0
        
        if topLeft == 0:
            for c in range(cols):
                matrix[0][c] = 0




                

                 
        
        