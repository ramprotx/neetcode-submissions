class Solution:

    def maxArea(self, heights: List[int]) -> int:
        'two pointers .move inward if smaller on the left and right'
        nums=len(heights)
        maxarea=0
        left=0
        right=nums-1
        while left < right :
            maxarea = max(maxarea, min(heights[left], heights[right]) * (right - left))
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return maxarea

    # def maxArea(self, heights: List[int]) -> int:
    #     res = 0
    #     for i in range(len(heights)):
    #         for j in range(i + 1, len(heights)):
    #             res = max(res, min(heights[i], heights[j]) * (j - i))
    #     return res