# Longest Repeating Character Replacement

### You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

### Return the length of the longest substring containing the same letter you can get after performing the above operations.

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

#### For the length of the window, keep a count of letters in it. For all letters, add the next letter to count, and if the range minus the maximum count of letteers in the set is bigger than k, move the left pointer and remove the letter. Return the maxLength. 