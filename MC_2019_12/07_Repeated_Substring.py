class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for sublen in range(1, len(s)):  # would be better to only take prime number
            if len(s) % sublen == 0:
                ok = True
                for sub_ind in range(len(s)//sublen):
                    if s[sub_ind * sublen: (sub_ind + 1) * sublen] != s[:sublen]:
                        ok = False
                if ok:
                    return True
        return False
