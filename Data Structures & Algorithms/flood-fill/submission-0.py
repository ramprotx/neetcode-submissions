class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        orig = image[sr][sc]             # the color we're replacing (the starting cell's color)

        if orig == color:                # already the target color: nothing changes
            return image                 # IMPORTANT: without this, dfs would never stop (see below)

        m, n = len(image), len(image[0]) # number of rows and columns

        def dfs(r, c):
            # stop if (r, c) is off the grid OR isn't part of the region
            # (a different color, or already repainted to `color`)
            if r < 0 or r >= m or c < 0 or c >= n or image[r][c] != orig:
                return

            image[r][c] = color          # paint this cell; this also marks it as visited,
                                         # because it no longer equals orig

            dfs(r + 1, c)                # spread down
            dfs(r - 1, c)                # spread up
            dfs(r, c + 1)                # spread right
            dfs(r, c - 1)                # spread left  (4 directions only, no diagonals)

        dfs(sr, sc)                      # start painting from the chosen cell
        return image                     # changed in place and returned