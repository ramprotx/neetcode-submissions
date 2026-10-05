class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        'count the chars and see if both count are same .'
        counts=Counter(s)
        hashmap_s={}
        hashmap_t={}
        for i in s:
            if i in hashmap_s:
                hashmap_s[i]=hashmap_s[i]+1
            else:
                hashmap_s[i]=1
        for i in t:
            if i in hashmap_t:
                hashmap_t[i]=hashmap_t[i]+1
            else:
                hashmap_t[i]=1
        return hashmap_s == hashmap_t