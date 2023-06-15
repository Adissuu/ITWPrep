# Valid parentheses

## Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

```
class Solution(object):
    def isValid(self, s):
        stack = []
        for c in s:
            if c in '([{':
                stack.append(c)
            else:
                if not stack or \
                    (c == ')' and stack[-1] != '(') or \
                    (c == '}' and stack[-1] != '{') or \
                        (c == ']' and stack[-1] != '['):
                    return False
                stack.pop()
        return not stack


class Solution2(object):
    def isValid(self, s):
        stack = []
        closeOpen = {')': '(', '}': '{', ']': '['}
        for c in s:
            if c in closeOpen:
                if stack and stack[-1] == closeOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False

```