class Solution:
    def rotateTheBox(self, boxGrid: list[list[str]]) -> list[list[str]]:
        ROWS, COLS = len(boxGrid), len(boxGrid[0])

        # the rotated box is COLS x ROWS; start with every cell empty
        res = [["."] * ROWS for _ in range(COLS)]

        # Rotating 90° clockwise maps (r, c) -> (c, ROWS - 1 - r):
        #   original column c   -> new row c
        #   original row r      -> new column ROWS - 1 - r  (the first row ends up as the LAST column)
        # After rotation "down" is the original "right", so stones slide toward higher c.

        for r in range(ROWS):                   # handle each original row on its own
            i = COLS - 1                        # i = lowest free spot (in original columns) a stone can land on;
                                                # starts at the far right = the bottom after rotation

            for c in reversed(range(COLS)):     # scan right to left = bottom to top after rotation
                if boxGrid[r][c] == "#":        # stone: it falls to the lowest free spot
                    res[i][ROWS - r - 1] = "#"  # place it at position i (not c), rotated
                    i -= 1                      # that spot is now taken; the next stone lands above it

                elif boxGrid[r][c] == "*":      # obstacle: it never moves
                    res[c][ROWS - r - 1] = "*"  # keep it at its own column c, rotated
                    i = c - 1                   # stones above it can only fall down to the obstacle,
                                                # so the next free spot is just above it

                # "." (empty): nothing to do, since res already holds "."

        return res