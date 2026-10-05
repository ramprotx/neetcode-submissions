class Solution:
    # def isAnagram(self, s: str, t: str) -> bool:
    #     if len(s) != len(t):
    #         return False
    #     s_count={}
    #     t_count={}
    #     for i in s:
    #         if i in s_count:
    #             s_count[i]+=1
    #         else:
    #             s_count[i]=1
        
    #     for i in t:
    #         if i in t_count:
    #             t_count[i]+=1
    #         else:
    #             t_count[i]=1

    #     for i in s_count:
    #         if i not in t_count or s_count[i]!=t_count[i]:
    #             return False
        
    #     return True

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT

    # def isAnagram(self, s: str, t: str) -> bool:
    #     if len(s) != len(t):
    #         return False

    #     count = [0] * 26
    #     for i in range(len(s)):
    #         count[ord(s[i]) - ord('a')] += 1
    #         count[ord(t[i]) - ord('a')] -= 1

    #     for val in count:
    #         if val != 0:
    #             return False
    #     return True
