class Solution:

    def overflow(self, x: int) -> int:
        if int(x) < -pow(2, 31) or int(x) > pow(2, 31) - 1:
            return 0
        return x

    def reverse(self, x: int) -> int:
        is_neg = x < 0
        if is_neg:
            return self.overflow("-" + str(int(str(x)[1:][::-1])))
        else:
            return self.overflow(int(str(x)[::-1]))
