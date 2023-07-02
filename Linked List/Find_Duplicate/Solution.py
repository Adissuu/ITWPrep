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
