class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxc = 0
        for sen in sentences:
            count = len(sen.split())
            maxc = max(count, maxc)
        return maxc