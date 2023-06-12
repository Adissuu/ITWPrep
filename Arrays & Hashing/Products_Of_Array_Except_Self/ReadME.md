# Products of array except self
### Given an array of numbers nums, return an array of numbers output such that output[i] is equal to the product of all the numbers in the array except nums[i].
```
# Time complexity: O(n)
# Space complexity: O(1) (two numbers)
class Solution(object):
    def productExceptSelf(self, nums):
        result = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)): #Loop forward
            result[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in  range(len(nums) - 1, -1, -1): #Loop backward
            result[i] *= suffix
            suffix *= nums[i]
        
        return(result)
```
### Solution description:
### We initialize the array with 1s. We then move through the array a first time and multiplying the prefix by the number i, except the first one since it doesn't have a prefix. We then pass a second time in the array, this time multiplying the suffix by the number i in the array.