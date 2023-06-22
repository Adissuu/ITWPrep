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
