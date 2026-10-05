class Solution:

    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""


    #  def minWindow(self, s: str, t: str) -> str:
    #     if t=="":
    #         return ""
        
    #     countT = {}
    #     for c in t:
    #         countT[c]=1+countT.get(c, 0)
        
    #     res, resLen=[-1,-1],float("infinity")

    #     for i in range(len(s)):
    #         countS={}
    #         for j in range(i, len(s)):
    #             countS[s[j]]=1+countS.get(s[j], 0)

    #             flag= True
    #             for c in countT:
    #                 if countT[c] > countS.get(c, 0):
    #                     flag=False
    #                     break
                
    #             if flag and (j-i+1)<resLen:
    #                 resLen=j-i+1
    #                 res=[i,j]
    #     l, r= res
    #     return s[l : r+1] if resLen !=float("infinity") else ""





    # def minWindow(self, s: str, t: str) -> str:
    #     if not t or not s:
    #         return ""
        
    #     dict_t = Counter(t)
    #     required = len(dict_t)
        
    #     l, r = 0, 0
    #     formed = 0
    #     window_counts = {}
        
    #     ans = float("inf"), None, None
        
    #     while r < len(s):
    #         character = s[r]
    #         window_counts[character] = window_counts.get(character, 0) + 1
            
    #         if character in dict_t and window_counts[character] == dict_t[character]:
    #             formed += 1
            
    #         while l <= r and formed == required:
    #             character = s[l]
    #             if r - l + 1 < ans[0]:
    #                 ans = (r - l + 1, l, r)
                
    #             window_counts[character] -= 1
    #             if character in dict_t and window_counts[character] < dict_t[character]:
    #                 formed -= 1
                
    #             l += 1    
            
    #         r += 1    
    #     return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]