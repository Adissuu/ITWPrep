# Largest Rectangle Histogram

## Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

```
# Time complexity: O(n)
# Space complexity: O(n)
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
```

### To picture this solution, let's say we traverse the array. Everytime we encounter a new value, if this value is bigger or the same as the precedent value in the stack, we append it to the stack and increment the index. However, if this is not the case, we pop every value that is bigger than the incoming value, while taking the area between the value and the incoming one (width). We then compute the rest present in the array.