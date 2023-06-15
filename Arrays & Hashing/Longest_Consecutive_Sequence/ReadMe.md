# Longest consecutive sequence

## 

```
class Solution(object):
    def longestConsecutive(self, nums):
        nums = list(set(nums))
        nums.sort()
        if len(nums) == 0: return 0
        count, result = 1, 1
        for i in range(len(nums) - 1):
            if nums[i + 1] == (nums[i] + 1):
                count += 1
                if result < count:
                    result = count
            else:
                if result < count:
                    result = count
                count = 1
        return result
```
