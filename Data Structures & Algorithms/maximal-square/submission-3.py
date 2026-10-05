class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        cache = {}                               # (r, c) -> side of the largest all-"1" square
                                                 # whose TOP-LEFT corner is (r, c)

        def helper(r, c):
            if r >= ROWS or c >= COLS:           # off the grid: no square can start here
                return 0

            if (r, c) not in cache:              # compute each cell only once
                down  = helper(r + 1, c)         # best square starting just below
                right = helper(r, c + 1)         # best square starting just to the right
                diag  = helper(r + 1, c + 1)     # best square starting diagonally down-right
                # these are called even when matrix[r][c] == "0", which is what makes
                # the recursion reach (and cache) EVERY cell in the grid

                cache[(r, c)] = 0                # a "0" cell can't start a square
                if matrix[r][c] == "1":
                    # a square of side k here needs squares of side k-1 at all three
                    # neighbors; the smallest neighbor limits how big this one can be
                    cache[(r, c)] = 1 + min(down, right, diag)

            return cache[(r, c)]

        helper(0, 0)                             # fills cache for every cell
        return max(cache.values()) ** 2 if cache else 0   # largest side, squared = area