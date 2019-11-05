class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s_new = s
        removed_set = set()
        for k in s:
            code = ord(k)
            if not ((code >= ord('a') and code <= ord('z'))
                    or (code >= ord('0') and code <= ord('9'))):
                removed_set.add(k)
        for c in removed_set:
            s = s.replace(c, '')
        return s == s[::-1]
