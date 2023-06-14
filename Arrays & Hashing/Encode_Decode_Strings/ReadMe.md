# Encode and decode Strings

## Desing an algorithm to encode a list of strings to a string, and an algorithm to decode a string into a list of strings.

```
#  Time: O(n)

class Solution(object):
    def encode(self, strs):
        encoded = ''
        for word in strs:
            encoded += str(len(word)) + "$" + word
        return encoded

    def decode(self, str):
        decoded = []
        i = 0

        while i < len(str):
            j = i
            while str[j] != "$":
                j += 1
            length = int(str[i:j])
            decoded.append(str[j + 1: j + 1 + length])
            i = j + 1 + length
        return decoded

```
### We simply add a $ sign as well as the supposed number of letters before the word appears in the string. In the decode function, we then simply have to look for the first $sign, which will have the number on its left. We convert the single character between i and j and convert it to a number, and we split the rest of the string with the converted length. We just have to add the index to i, verify that it is not done, and return the list.