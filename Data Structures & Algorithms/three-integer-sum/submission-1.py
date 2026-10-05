class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        'sort and  two number add result negative ,then add 3rd positive number to get 0.if result is positive -same amountto get zero'
        sortvalue=sorted(nums)
        res = []
        for i in range(len(sortvalue)-2):
            if i > 0 and sortvalue[i] == sortvalue[i-1]:
                continue
            l, r = i + 1, len(sortvalue) - 1
            while l < r:
                s = sortvalue[i] + sortvalue[l] + sortvalue[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append([sortvalue[i], sortvalue[l], sortvalue[r]])
                    while l < r and sortvalue[l] == sortvalue[l+1]:
                        l += 1
                    while l < r and sortvalue[r] == sortvalue[r-1]:
                        r -= 1
                    l += 1; r -= 1
        return res