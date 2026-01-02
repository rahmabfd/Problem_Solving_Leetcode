class Solution(object):
    def commonChars(self, words):
        freq = Counter(words[0])

        for word in words[1:]:
            freq &= Counter(word)   

        res = []
        for ch, count in freq.items():
            res.extend([ch] * count)

        return res
