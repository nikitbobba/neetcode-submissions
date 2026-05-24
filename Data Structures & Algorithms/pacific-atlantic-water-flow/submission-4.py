class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        ROW, COL = len(heights), len(heights[0])
        pacific = [[False] * COL for _ in range(ROW)]
        atlantic = [[False] * COL for _ in range(ROW)]

        def bfs(state, ocean):
            # This function will receive all the cells that border an ocean and
            # the ocean grid
            q = deque(state)
            while len(q) != 0:
                r, c = q.popleft()
                ocean[r][c] = True # since this cell leads to the ocean
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    # Add possible next directions to queue
                    if 0 <= nr < ROW and 0 <= nc < COL and ocean[nr][nc] == False and heights[nr][nc] >= heights[r][c]:
                        q.append((nr, nc))
            
        
        pacificBorders = []
        atlanticBorders = []
        
        for i in range(COL):
            pacificBorders.append((0,i))
            atlanticBorders.append((ROW-1, i))
        
        for i in range(ROW):
            pacificBorders.append((i,0))
            atlanticBorders.append((i,COL-1))
        
        bfs(pacificBorders, pacific)
        bfs(atlanticBorders, atlantic)

        res = []
        for r in range(ROW):
            for c in range(COL):
                if pacific[r][c] and atlantic[r][c]:
                    res.append((r,c))
        return res
                    

                    

                    



        