class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        ROW, COL = len(grid), len(grid[0]) 
        print('here')
        
        def bfs(r, c):
            q = deque()

            q.append((r,c))
            grid[r][c] = '0'

            while len(q) != 0:
                r, c = q.popleft()
                for dr, dc in directions:
                    if 0 <= (r+dr) < ROW and 0 <= (c+dc) < COL and grid[r+dr][c+dc] == '1':
                        # add to the queue
                        q.append((r+dr, c+dc))
                        grid[r+dr][c+dc] = '0'
                    else:
                        continue
        islands = 0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == '1':
                    bfs(r, c)
                    islands += 1
        
        return islands

