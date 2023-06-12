# Time complexity: O(n)
# Space complexity: O(1) (two numbers)
class Solution(object):
    def productExceptSelf(self, nums):
        result = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):  # Loop forward
            result[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(len(nums) - 1, -1, -1):  # Loop backward
            result[i] *= suffix
            suffix *= nums[i]

        return(result)
