from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        open_signs = ['{', '[', '(']
        close_signs = ['}', ']', ')']
        possible = True
        for c in s:
            if c in open_signs:
                stack.appendleft(c)
            else:
                if not stack:
                    possible = False
                    break
                matching_char = stack.popleft()
                if matching_char != open_signs[close_signs.index(c)]:
                    possible = False
                    break
        if stack:
            possible = False
        return possible
