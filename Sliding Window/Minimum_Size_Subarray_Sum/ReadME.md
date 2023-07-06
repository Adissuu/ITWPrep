# Minimum Size Subarray Sum

### Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

```
# Time Complexity: O(nlogn)
# Space Complexity: O(1)
class Solution(object):
    def minSubArrayLen(self, target, nums):
        left, right, sum = 0, 0, 0
        maximum = 1000000
        minimum = maximum
        
        
        while right < len(nums):
            sum += nums[right]
            while sum >= target:
                minimum = min(minimum, right - left + 1)
                sum -= nums[left]
                left += 1
            right += 1
        return 0 if minimum == maximum else minimum

```

#### Find the shortest subarray in the given array whose sum is equal to or greater than the target value by using two pointers that expand the window by moving the right pointer, finds the minimum length by adjusting the left pointer, and keeps track of the smallest length encountered so far.