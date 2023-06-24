# Three sum

### Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

```
class Solution(object):
    def threeSum(self, nums):
        result = []
        nums.sort()
        for i, num in enumerate(nums):
            if num > 0:
               break
            if i > 0 and num == nums[i-1]:
                continue

            j, k = i + 1, len(nums) - 1
            while k > j:
                threesum = num + nums[j] + nums[k]
                if threesum > 0:
                    k -=1s
                elif threesum < 0:
                    j += 1
                else:
                    result.append([num, nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
        return result
```

### Sort the array so that we can traverse it more easily. Then, for each number present in the array, do a two sum on its left part. If the number is positive, there is no way the second could be, so we break.s
