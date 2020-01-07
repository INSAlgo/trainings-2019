class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        sum_shift = 0
        s = list(S)
        index = len(shifts) - 1
        for shift in shifts[::-1]:
            sum_shift += shift % 26
            s[index] = chr((ord(s[index])-ord('a') + sum_shift) %
                           26 + ord('a'))
            index -= 1
        return "".join(s)
