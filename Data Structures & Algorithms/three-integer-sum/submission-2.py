class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res



    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     nums.sort()
    #     count = defaultdict(int)
    #     for num in nums:
    #         count[num] += 1

    #     res = []
    #     for i in range(len(nums)):
    #         count[nums[i]] -= 1
    #         if i and nums[i] == nums[i - 1]:
    #             continue

    #         for j in range(i + 1, len(nums)):
    #             count[nums[j]] -= 1
    #             if j - 1 > i and nums[j] == nums[j - 1]:
    #                 continue
    #             target = -(nums[i] + nums[j])
    #             if count[target] > 0:
    #                 res.append([nums[i], nums[j], target])

    #         for j in range(i + 1, len(nums)):
    #             count[nums[j]] += 1
    #     return res


    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     res = set()
    #     nums.sort()
    #     for i in range(len(nums)):
    #         for j in range(i + 1, len(nums)):
    #             for k in range(j + 1, len(nums)):
    #                 if nums[i] + nums[j] + nums[k] == 0:
    #                     tmp = [nums[i], nums[j], nums[k]]
    #                     res.add(tuple(tmp))
    #     return [list(i) for i in res]

    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     'sort and  two number add result negative ,then add 3rd positive number to get 0.if result is positive -same amountto get zero'
    #     sortvalue=sorted(nums)
    #     res = []
    #     for i in range(len(sortvalue)-2):
    #         if i > 0 and sortvalue[i] == sortvalue[i-1]:
    #             continue
    #         l, r = i + 1, len(sortvalue) - 1
    #         while l < r:
    #             s = sortvalue[i] + sortvalue[l] + sortvalue[r]
    #             if s < 0:
    #                 l += 1
    #             elif s > 0:
    #                 r -= 1
    #             else:
    #                 res.append([sortvalue[i], sortvalue[l], sortvalue[r]])
    #                 while l < r and sortvalue[l] == sortvalue[l+1]:
    #                     l += 1
    #                 while l < r and sortvalue[r] == sortvalue[r-1]:
    #                     r -= 1
    #                 l += 1; r -= 1
    #     return res