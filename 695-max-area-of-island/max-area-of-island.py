class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        column = len(grid[0])
        max_area = 0
        for r in range(rows):
            for c in range(column):
                if grid[r][c] == 1:
                    area = 0
                    queue = deque()
                    queue.append((r, c))
                    grid[r][c] = 0
                    while queue:
                        i, j = queue.popleft()
                        area += 1
                        for dx, dy in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                            new_i = i + dx
                            new_j = j + dy
                            if new_i < 0 or new_i >= rows or new_j < 0 or new_j >= column:
                                continue
                            if grid[new_i][new_j] != 1:
                                continue
                            grid[new_i][new_j] = 0
                            queue.append((new_i, new_j))
                    max_area = max(max_area, area)
        return max_area