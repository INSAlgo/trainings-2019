class Solution:
    def palindrome(self, s: str) -> bool:
        return s == s[::-1]

    def validPalindrome(self, s: str) -> bool:
        ind_start = 0
        ind_end = len(s)
        while(ind_end - ind_start > 1):
            if s[ind_start] != s[ind_end - 1]:
                res = self.palindrome(
                    s[ind_start + 1:ind_end]) \
                    or self.palindrome(s[ind_start:ind_end - 1])
                return res
            ind_start += 1
            ind_end -= 1
        return True
