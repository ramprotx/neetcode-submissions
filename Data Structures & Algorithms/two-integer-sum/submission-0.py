class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for index, i in enumerate(nums):
            temp=target-i
            if temp in hashmap:
                return [hashmap[temp], index]
            hashmap[i] = index