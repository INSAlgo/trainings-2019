class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mapping = {}
        mapped = set()
        for k in range(len(s)):
            # the letter is already mapped, and not matching
            if s[k] in mapping and t[k] != mapping[s[k]]:
                return False
            # not mapped yet
            if s[k] not in mapping:
                # check that the mapping is a one to one
                if t[k] in mapped:
                    return False
                else:
                    # include in mapping
                    mapping[s[k]] = t[k]
                    mapped.add(t[k])
        return True
