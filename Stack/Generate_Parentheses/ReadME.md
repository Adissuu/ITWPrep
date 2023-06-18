# Generate parentheses

## Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

```
class Solution(object):
    def generateParenthesis(self, n):
        stack = []
        result = []

        def backtrack(openCount, closedCount):
            if openCount == closedCount == n:
                result.append("".join(stack))
                return
            if openCount < n:
                stack.append("(")
                backtrack(openCount + 1, closedCount)
                stack.pop()
            if closedCount < openCount:
                stack.append(")")
                backtrack(openCount, closedCount + 1)
                stack.pop()
        backtrack(0, 0)
        return result
```

### I created a stack for temporary strings and a result for, well... handing out the solution. I then created a recursive function that looks if the temporary stack is done, with all parentheses added. If so, this stack will be appended to result, and the temporary stack will pop the last added parenthese(s) and continue on its merry way. 

### Example with n = 3:
```
--> backtrack(0, 0)
--> if openCount == closedCount == n: false
--> if openCount < n: true 
--> stack=["("]
--> backtrack(1, 0)
--> if openCount == closedCount == n: false
--> if openCount < n: true 
--> stack=["(", "("]
--> backtrack(2, 0)
--> if openCount == closedCount == n: false
--> if openCount < n: true 
--> stack=["(", "(", "("]
--> backtrack(3, 0)
--> if openCount == closedCount == n: false
--> if openCount < n: false 
--> if closedCount < openCount: true
--> stack=["(", "(", "(", ")"]
--> backtrack(3, 1)
--> if openCount == closedCount == n: false
--> if openCount < n: false 
--> if closedCount < openCount: true
--> stack=["(", "(", "(", ")", ")]
--> backtrack(3, 2)
--> if openCount == closedCount == n: false
--> if openCount < n: false 
--> if closedCount < openCount: true
--> stack=["(", "(", "(", ")", "), ")"]
--> backtrack(3, 3)
--> if openCount == closedCount == n: true
--> result=["((()))"]
--> stack=["(", "(", "(", ")", ")"]
--> stack=["(", "(", "(", ")"]
--> stack=["(", "(", "("]
--> stack=["(", "("]
--> if closedCount < openCount: true
--> stack=["(", "(", ")"]
--> etc....
```