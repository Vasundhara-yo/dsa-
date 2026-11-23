class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])

        queue = deque()
        grid_copy = deepcopy(grid)
        fresh_orange = 0

        for r in range(rows):
            for c in range(columns):
                if grid_copy[r][c] == 2:
                    queue.append((r, c))
                elif grid_copy[r][c] == 1:
                    fresh_orange += 1

        minutes = 0

        while queue and fresh_orange > 0:
            total_rotten = len(queue)
            rotted = False

            for _ in range(total_rotten):
                i, j = queue.popleft()

                for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                    new_i = i + dx
                    new_j = j + dy

                    if (new_i < 0 or new_i >= rows or
                        new_j < 0 or new_j >= columns):
                        continue

                    if grid_copy[new_i][new_j] != 1:
                        continue

                    fresh_orange -= 1
                    grid_copy[new_i][new_j] = 2
                    queue.append((new_i, new_j))
                    rotted = True

            if rotted:
                minutes += 1

        if fresh_orange > 0:
            return -1

        return minutes

        