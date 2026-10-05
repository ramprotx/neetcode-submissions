class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left=0
        n=len(matrix)
        right=n-1
        while left<=right:
            mid=(left+right)//2
            if target < matrix[mid][0]:
                right=mid-1
            elif target > matrix[mid][-1]:
                left=mid+1
            else:
                return target in matrix[mid]
        return False

    #  def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    #     for r in range(len(matrix)):
    #         for c in range(len(matrix[0])):
    #             if matrix[r][c] == target:
    #                 return True
    #     return False
