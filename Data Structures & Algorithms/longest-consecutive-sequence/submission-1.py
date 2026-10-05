class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset={}
        hashset=set(nums)
        maxLen=0
        
        for x in hashset:
            currSeqLen=0
            if not x-1 in hashset:                
                while x + currSeqLen in hashset:
                    currSeqLen += 1
            if currSeqLen>maxLen:
                maxLen=currSeqLen
        return maxLen