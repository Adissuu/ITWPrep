def groupAnagrams(self, strs):
    results = {}  # map chars
    for word in strs:
        sorted_word = "".join(sorted(word))
        if sorted_word in results:
            results[sorted_word].append(word)
        else:
            results[sorted_word] = [word]
    return results.values()
