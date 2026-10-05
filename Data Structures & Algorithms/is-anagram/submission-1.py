class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_count={}
        t_count={}
        for i in s:
            if i in s_count:
                s_count[i]+=1
            else:
                s_count[i]=1
        
        for i in t:
            if i in t_count:
                t_count[i]+=1
            else:
                t_count[i]=1

        for i in s_count:
            if i not in t_count or s_count[i]!=t_count[i]:
                return False
        
        return True
