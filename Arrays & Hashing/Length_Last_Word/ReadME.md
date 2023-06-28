# Length last word

### Given a string s consisting of words and spaces, return the length of the last word in the string.

```
# Time complexity: O(n)
# Space complexity: O(1)
class Solution(object):
    def lengthOfLastWord(self, s):
        return len(s.split()[-1])
```

#### Take the last word with s.split[-1], and return its length.