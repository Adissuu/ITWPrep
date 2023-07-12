class Solution(object):
    def minWindow(self, s, t):
        # edge case
        if t == "":
            return ""

        countT, window = {}, {}
        for i in range(len(t)):  # hashmap for t
            countT[t[i]] = 1 + countT.get(t[i], 0)

        current, obj = 0, len(countT)
        ptrs, length = [0, 0], float('inf')
        l = 0
        # add the char at r in the window hashmap and increment the count
        # when we get to the desired value, save the value and move l until the condition is not satisfied
        # return the min
        for r in range(len(s)):
            char = s[r]
            window[char] = 1 + window.get(char, 0)

            if char in countT and window[char] == countT[char]:
                current += 1

            while current == obj:
                if (r - l + 1) < length:
                    ptrs = [l, r]
                    length = r - l + 1
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    current -= 1
                l += 1
        l, r = ptrs
        return s[l: r + 1] if length != float("inf") else ""
