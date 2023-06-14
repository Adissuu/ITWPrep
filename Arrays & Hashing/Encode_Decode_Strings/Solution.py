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
