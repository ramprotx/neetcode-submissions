class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        'sliding window.if duplicate skip the 1st left value and move to 1 right value .check again and repeat'
        'hashtable'
        seen={}
        left=0
        n=len(s)

        max_len=0
        for right in range(n):
            if s[right] in seen and seen[s[right]] >= left:
                left = seen[s[right]] + 1
            seen[s[right]] = right
            max_len = max(max_len, right - left + 1)
        return max_len