from collections import deque
from typing import List

class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        rows, cols = len(mat), len(mat[0])
        visited = [[0]*cols for _ in range(rows)]
        distance = [[0]*cols for _ in range(rows)]
        queue = deque()

        # 1. Enqueue all zeros as BFS sources
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append((r, c, 0))
                    visited[r][c] = 1

        # 2. BFS from all zeros simultaneously
        while queue:
            i, j, d = queue.popleft()
            distance[i][j] = d
            # Visit four directions
            for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
                ni, nj = i + di, j + dj
                # Skip out of bounds or already visited
                if (0 <= ni < rows and 0 <= nj < cols 
                        and visited[ni][nj] == 0):
                    visited[ni][nj] = 1
                    queue.append((ni, nj, d+1))

        return distance
        