class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for i, n in enumerate(nums):
            if target - n in prevMap:
                return [prevMap[target - n], i]
            else:
                prevMap[n]=i

        return []       
           
       
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
           
    #     for i in range(len(nums)):
    #         for j in range(i+1,len(nums)):
    #             if nums[i]+nums[j]==target and i!=j:
    #                 return [i,j]
    #     return []


    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     hashmap={}
    #     for index, i in enumerate(nums):
    #         temp=target-i
    #         if temp in hashmap:
    #             return [hashmap[temp], index]
    #         hashmap[i] = index