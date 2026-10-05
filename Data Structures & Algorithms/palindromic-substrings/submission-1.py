class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        # Every palindrome has a center. Try every possible center in the string.
        for i in range(len(s)):
            # Odd-length palindromes: center is a single character (l = r = i)
            # e.g. "aba" is centered on 'b'
            res += self.countPali(s, i, i)

            # Even-length palindromes: center sits between two characters (l = i, r = i + 1)
            # e.g. "abba" is centered between the two 'b's
            res += self.countPali(s, i, i + 1)
        return res

    def countPali(self, s, l, r):
        res = 0
        # Expand outward from the center as long as:
        #   - l hasn't fallen off the left edge
        #   - r hasn't fallen off the right edge
        #   - the characters at both ends match (so the substring is still a palindrome)
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1   # each successful expansion is one new palindromic substring
            l -= 1     # move left pointer outward
            r += 1     # move right pointer outward
        # Return how many palindromes were found around this center
        return res