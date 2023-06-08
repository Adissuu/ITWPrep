class Solution(object):
    def isAnagram(self, s, t):
        ls = list(s)
        lt = list(t)
        ls.sort()
        lt.sort()
        return ls == lt
