# Trapping rain water

### Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

```
# Time complexity: O(n)
# Space complexity: O(1)
class Solution(object):
    def trap(self, height):
        result = 0

        l, r  = 0, len(height) - 1 
        maxL, maxR = height[l], height[r]
        
        while l < r:
            if maxL <= maxR:
                l += 1
                maxL = max(maxL, height[l])
                result += maxL - height[l]
            else:
                r -=1
                maxR = max(maxR, height[r])
                result += maxR - height[r]
        return result
```

#### After understanding the solution, this problem becomes quite easy. First of all, we want to keep track of the maximum amount of water one index can have. In order to do that, we simply need the height of that index, and the minimum on its left and right. If we put two pointers and keep track of that said minimum, we can cover the whole array by increasing the index of the lower "wall" of that array. We then add the height of the wall minus the height of the index (if it is a max we add 0) and continue our iteration.