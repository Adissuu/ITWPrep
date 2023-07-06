# Time Complexity: O(nlogn)
# Space Complexity: O(1)
class Solution(object):
    def minSubArrayLen(self, target, nums):
        left, right, _sum = 0, 0, 0
        maximum = 1000000
        minimum = maximum

        while right < len(nums):
            _sum += nums[right]
            while _sum >= target:
                minimum = min(minimum, right - left + 1)
                _sum -= nums[left]
                left += 1
            right += 1
        return 0 if minimum == maximum else minimum
