class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d_index = {}
        current_start = -1
        max_len = 0
        for k in range(len(s)):
            if s[k] not in d_index:
                d_index[s[k]] = k
            else:
                if d_index[s[k]] > current_start:
                    # cut the substring to after the last occurence of the character
                    current_start = d_index[s[k]]
                d_index[s[k]] = k
            max_len = max(max_len, k - current_start)

        return max_len
