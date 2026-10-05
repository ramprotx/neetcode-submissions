# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         s = str(x)
#         n = len(s)
#         for i in range(n // 2):
#             if s[i] !=s[n-i-1]:
#                 return False
#         return True
        

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are never palindromes (the '-' sign breaks it)
        # Also, any positive number ending in 0 (except 0 itself) can't be a palindrome
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reverted = 0
        while x > reverted:
            reverted = reverted * 10 + x % 10
            x //= 10

        # Even-length numbers: x == reverted
        # Odd-length numbers: middle digit is irrelevant, so x == reverted // 10
        return x == reverted or x == reverted // 10