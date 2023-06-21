class Solution(object):
    def largestRectangleArea(self, heights):
        stack = []
        result = 0
        for index, value in enumerate(heights):
            start = index
            while stack and stack[-1][1] > value:
                indexPopped, valuePopped = stack.pop()
                result = max(result, valuePopped * (index - indexPopped))
                start = indexPopped
            stack.append((start, value))

        for index, value in stack:
            result = max(result, value * (len(heights) - index))
        return result
