class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Rotate an n x n matrix by 90 degrees clockwise, in place.

        :param matrix: List of lists of integers, representing an n x n matrix.
        :return: None. The input matrix is modified in place.
        """
        # TODO: implement
        # in place .no addition matrix
        l, r = 0, len(matrix) - 1
        while l < r:
            for i in range(r - l):
                top, bottom = l, r
                
                topLeft = matrix[top][l + i]
                matrix[top][l + i] = matrix[bottom - i][l]
                matrix[bottom - i][l] = matrix[bottom][r - i]
                matrix[bottom][r - i] = matrix[top + i][r]
                matrix[top + i][r] = topLeft
            r -= 1
            l += 1