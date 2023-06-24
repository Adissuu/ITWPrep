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
