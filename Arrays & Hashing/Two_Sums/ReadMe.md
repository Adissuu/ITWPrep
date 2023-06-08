# Two Sums

### Given an array of integer nums, find the two indexes that add up to the target
```
class Solution(object):
    def twoSum(self, nums, target):
        prevSet = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevSet:
                return [prevSet[diff], i]
            prevSet[n] = i

```

#### The choice of using a dictionary in the code block is because it is a balance between time and space complexity. We create a dictionary that will give us the opportunity of quickly searching if there is a corresponding number to complete the sum.