# Longest Substring Without Repeating Characters

### Given a string s, find the length of the longest 

```
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        chars = list(s)
        print(chars)
        if len(chars) == 0: return 0
        if len(chars) == 1: return 1

        l, r, length = 0, 1, 0
        while r < len(chars):
           
            if chars[r] in chars[l:r]:
                length = max(length, r - l)
                print(chars[l:r])
                l = r
            r += 1
            length = max(length, r - l)
        return length
```
