# Two Sum II - Input Array Is Sorted
### Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.

```
class Solution(object):
    def twoSum(self, numbers, target):
        l, r = 0, len(numbers) - 1

        while (numbers[l] + numbers[r]) != target: 
            if numbers[l] + numbers[r] > target:
                r -= 1
            else:
                l += 1
        return [l+1, r+1]
```

#### To see it in a more optimized way, since that array is already sorted, we can simply use the check of the sum. If it is bigger than the target number, reduce right endpoint. If not, increase left endpoint. 