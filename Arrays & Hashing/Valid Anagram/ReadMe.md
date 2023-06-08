# Valid Anagram

### Given two strings s and t, write a function to determine if t is an anagram of s
```
class Solution(object):
    def isAnagram(self, s, t):
        ls = list(s)
        lt = list(t)
        ls.sort()
        lt.sort()
        return ls == lt
```

By turning s and t into lists and sorting them, we can then verify if they are the same and if they are therefore an anagram.