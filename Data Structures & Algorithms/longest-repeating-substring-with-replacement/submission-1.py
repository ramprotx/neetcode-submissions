class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        'sliding window'
        'hashmap,set with chars count'    
        
        charCount={}
        left=0        
        n=len(s)
        max_length=0
        frequency_of_most_frequent_char=0
        'get the most repetitive character frequency_of_most_frequent_char'      
        
        for right in range(n):
            charCount[s[right]] = charCount.get(s[right], 0) + 1
            frequency_of_most_frequent_char = max(frequency_of_most_frequent_char, charCount[s[right]])
            
            if (right - left + 1) - frequency_of_most_frequent_char > k:
                charCount[s[left]] -= 1
                left += 1
            
            max_length = max(max_length, right - left + 1)

        return max_length