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
