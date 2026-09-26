class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        result = Counter(words[0])
        for word in words[1:]:
            result &= Counter(word)
        return list(result.elements())

                
