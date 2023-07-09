# Longest Repeating Character Replacement

### Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

```
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution(object):
    def characterReplacement(self, s, k):
        count = {}
        maxLength = 0

        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            if (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            maxLength = max(maxLength, r - l + 1)

        return maxLength

```

#### Find the shortest subarray in the given array whose sum is equal to or greater than the target value by using two pointers that expand the window by moving the right pointer, finds the minimum length by adjusting the left pointer, and keeps track of the smallest length encountered so far.