# Find duplicate number in array

### Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

### There is only one repeated number in nums, return this repeated number.

### You must solve the problem without modifying the array nums and uses only constant extra space.

```
# Time complexity: O(n)
# Space complexity: O(1)
class Solution(object):
    def findDuplicate(self, nums):
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                slow2 = 0
                while True:
                    slow = nums[slow]
                    slow2 = nums[slow2]
                    if slow == slow2:
                        return slow

```

#### We need to see the array as a linked list. The number in the index represents the index of the next number. When the fast and slow pointers have the same value, it means that they're in a loop. Then, following Floyd's algorithm, if we start back with two slow pointers, the intersection between the new slow and the past one reveals the number that is duplicated.