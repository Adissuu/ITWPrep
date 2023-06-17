# Evaluate reverse polish notation

## You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

```
# Time complexity: O(n)
# Space complexity: O(n)
class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        for c in tokens:
            if c not in "+-*/":
                stack.append(int(c))
            else:
                n1, n2 = stack.pop(), stack.pop()
                if c == "+":
                    stack.append(n2+n1)
                elif c == "-":
                    stack.append(n2-n1)
                elif c == "*":
                    stack.append(n2*n1)
                else:
                    stack.append(int(float(n2)/n1))
        return stack.pop()
```

###  Verify if the element is an operation, and if so, pop the last two elements and perform the operation. Straightforward.