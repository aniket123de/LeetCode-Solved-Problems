class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        words = s.split()
        sentence = ''
        for i in range(k):
            sentence += words[i] + ' '
        sentence = sentence.strip()
        return sentence