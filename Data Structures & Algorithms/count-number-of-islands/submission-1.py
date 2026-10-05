class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # The four neighbor offsets: down, up, right, left
        directions = [[1,0], [-1,0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def dfs(r, c):
            # Base case: stop if out of bounds OR the cell is water/already visited
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == "0"):
                return
            # Mark this land cell as visited by "sinking" it to water
            grid[r][c] = "0"
            # Spread to all four neighbors to sink the rest of the island
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        # Scan every cell in the grid
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":   # Found an unvisited piece of land
                    dfs(r, c)           # Sink the entire island it belongs to
                    islands += 1        # Count it once
        return islands