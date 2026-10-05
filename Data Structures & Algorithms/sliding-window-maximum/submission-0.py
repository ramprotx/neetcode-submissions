class Solution:

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque()  # index
        l = r = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output
        
    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #     output=[]

    #     for i in range(len(nums) -k +1):
    #         maxi=nums[i]
    #         for j in range(i,i+k):
    #             maxi=max(maxi, nums[j])
    #         output.append(maxi)

    #     return output


        