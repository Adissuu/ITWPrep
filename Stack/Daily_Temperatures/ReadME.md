# Daily temperatures

## Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

```
# Time complexity: O(n)
# Space complexity: O(n)
class Solution(object):
    def dailyTemperatures(self, temperatures):
        result = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackTemp, stackIndex = stack.pop()
                result[stackIndex] = (i - stackIndex)
            stack.append([temp, i])
        return result
```

###  This one is a bit hard to picture at first, but it then becomes clearer: We initialize a temperature array, and for each temperature in temperatures, if the stack if not empty and the value at the top is smaller than the current temperature, we pop the stack, and register the current index - the index saved in the popped stack, and we then append the current temperature with its index.