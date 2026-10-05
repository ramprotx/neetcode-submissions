class Solution:

    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res



    # def characterReplacement(self, s: str, k: int) -> int:
    #     res = 0
    #     charSet = set(s)

    #     for c in charSet:
    #         count = l = 0
    #         for r in range(len(s)):
    #             if s[r] == c:
    #                 count += 1

    #             while (r - l + 1) - count > k:
    #                 if s[l] == c:
    #                     count -= 1
    #                 l += 1

    #             res = max(res, r - l + 1)
    #     return res


    # def characterReplacement(self, s: str, k: int) -> int:
    #     res=0
    #     for i in range(len(s)):
    #         count, maxf={}, 0
    #         for j in range(i,len(s)):
    #             count[s[j]]=1+count.get(s[j],0)
    #             maxf=max(maxf, count[s[j]])
    #             if(j-i+1)-maxf<=k:
    #                 res=max(res,j-i+1)
    #     return res

        

    # def characterReplacement(self, s: str, k: int) -> int:
    #     'sliding window'
    #     'hashmap,set with chars count'    
        
    #     charCount={}
    #     left=0        
    #     n=len(s)
    #     max_length=0
    #     frequency_of_most_frequent_char=0
    #     'get the most repetitive character frequency_of_most_frequent_char'      
        
    #     for right in range(n):
    #         charCount[s[right]] = charCount.get(s[right], 0) + 1
    #         frequency_of_most_frequent_char = max(frequency_of_most_frequent_char, charCount[s[right]])
            
    #         if (right - left + 1) - frequency_of_most_frequent_char > k:
    #             charCount[s[left]] -= 1
    #             left += 1
            
    #         max_length = max(max_length, right - left + 1)
