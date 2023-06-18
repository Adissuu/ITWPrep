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
