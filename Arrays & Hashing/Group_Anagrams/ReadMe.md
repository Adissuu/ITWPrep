# Group Anagrams

### Given an array of strings, group anagrams together.
```
# Time complexity: O(m*nlogn)
# O(n)
def groupAnagrams(self, strs):
    results = {}  # map chars
    for word in strs:
        sorted_word = "".join(sorted(word))
        if sorted_word in results:
            results[sorted_word].append(word)
        else:
            results[sorted_word] = [word]
    return results.values()
```

#### This solution is a bit more complex. We initialize an empty dictionnaty and create sorted strings for each words present in the list for it to be appended in the results as the key. If it is already in, simply append the original word. If not, then create a key and add the original word.