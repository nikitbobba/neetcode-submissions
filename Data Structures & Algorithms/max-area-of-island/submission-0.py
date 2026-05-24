class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[0,1], [0,-1], [1, 0], [-1, 0]]

        ROW, COL = len(grid), len(grid[0])

        maxIsland = 0

        def bfs(r,c):
            q = deque()
            grid[r][c] = 0
            q.append((r,c))
            islandSize = 0
            while len(q) != 0:
                r, c = q.popleft()
                islandSize += 1
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROW and 0 <= nc < COL and grid[nr][nc] == 1:
                        # an adiitional cell
                        q.append((nr, nc))
                        grid[nr][nc] = 0
            
            return islandSize
        
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    size = bfs(r, c)
                    maxIsland = max(maxIsland, size)

        return maxIsland
                


        