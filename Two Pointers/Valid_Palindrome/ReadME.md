# Valid Palindrome

###  A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

```
class Solution(object):
    def isPalindrome(self, s):
        alphabet = "abcdefghijklmnopqrstuvwxyz1234567890"
        palindrome = []
        for letter in s:
            if letter.lower() in alphabet:
                palindrome.append(letter.lower())
        p1, p2 = 0, len(palindrome) - 1
        while p1 < p2:
            if palindrome[p1] != palindrome[p2]:
                return False
            p1 += 1
            p2 -= 1
        return True
```

#### For every letter in the string, if it is an alphanumerical character, add it to an array. Then iterate through the array from the beginning and the end and look if both end match constantly.