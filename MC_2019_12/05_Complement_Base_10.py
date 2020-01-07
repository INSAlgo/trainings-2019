class Solution:
    def bitwiseComplement(self, N: int) -> int:
        bin_representation = bin(N)[2:]
        bin_result = ""
        for b in bin_representation:
            if b == "0":
                bin_result += "1"
            else:
                bin_result += "0"
        return int(bin_result, 2)
