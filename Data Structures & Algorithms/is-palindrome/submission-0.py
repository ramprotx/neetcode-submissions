class Solution:
    def isPalindrome(self, s: str) -> bool:
        'if total char len is odd '
        'get mid index of total length.Two pointers left startig from 0 and right starting from len-1 whcih is last  and compare the chars'
        'if total char len is even then do the needful'
        left=0
        right=len(s)-1
        while left<right:
            if not s[left].isalnum():
                left+=1
                continue
            if not s[right].isalnum():
                right-=1
                continue
            if not s[left].lower()==s[right].lower():
                return False
            else:
                left+=1
                right-=1
        return True
