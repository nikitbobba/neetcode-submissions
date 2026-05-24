class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW, COL = len(grid), len(grid[0])
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        q = deque()
        # Add all the treasure to the queue
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    q.append((r,c))
        # BFS to mark all the possible spots on the grid            

        while len(q) != 0:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                # Only valid next directions via grid dimensions
                if 0 <= nr < ROW and 0 <= nc < COL and grid[nr][nc] != -1:
                    if grid[nr][nc] == 2147483647:
                        grid[nr][nc] = grid[r][c] + 1
                        q.append((nr, nc))
        
        







        