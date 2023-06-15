# Longest consecutive sequence

## Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence. You must write an algorithm that runs in O(n) time.

### Here is my first solution:
```
# Time Complexity: O(nlogn)
# Space Complexity: O(n)
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
### Unfortunately, the algorithms to sort the nums, whether we use merge sort or quicksort, is at least O(nlogn), which rejects the solution.

### Here is my second solution:
```
class Solution(object):
    def longestConsecutive(self, nums):
        result = 0
        nums = set(nums)
        for num in nums:
            if (num - 1) not in nums:
                length = 0
                while (num + length) in nums:
                    length += 1
                result = max(result, length)
        return result
```
### This solution has a time complexity of O(n) since it goes in the array only once, and it takes n to convert a list into a set. In this algorithm, I transform the list in a set and I then verify which number doesn't have itself - 1 in the set, and if so, how many numbers come after it. By the end of that enumeration I compare to the max length I already have stored, and I return the max.