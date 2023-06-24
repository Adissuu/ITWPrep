# Container with most water

### You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

### Find two lines that together with the x-axis form a container, such that the container contains the most water.

### Return the maximum amount of water a container can store.

```
class Solution(object):
    def maxArea(self, height):
        l, r = 0, len(height) - 1
        result = 0
        # Two pointers
        while l < r:
            minHeight = min(height[l], height[r])
            result = max(result, minHeight * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return result
```

#### This problem becomes easier when you get used to the Two Pointers problems. In this case, we initialize two endpoints, left and right, and we compute the maximum amount of water between two indexes. This is done by first calculating the minimum between two heights, and multiply that value by the number of indexes between the two points. We then close up the gap by changing the index of the lower height.
