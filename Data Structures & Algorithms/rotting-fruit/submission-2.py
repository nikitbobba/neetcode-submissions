class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        directions = [[0,1], [1,0], [0,-1], [-1,0]]
        visit = [[0] * COL for _ in range(ROW)]
        q = deque()
        # load the queue with all the rotten fruit
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 2:
                    q.append((r,c))
        
        while len(q) != 0:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if 0<=nr<ROW and 0<=nc<COL and grid[nr][nc] == 1:
                    grid[nr][nc] = 0
                    visit[nr][nc] = visit[r][c] + 1
                    q.append((nr,nc))
        
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    return -1
        maxVal = 0
        for r in range(ROW):
            for c in range(COL):
                maxVal = max(maxVal, visit[r][c])
        
        return maxVal
            
        