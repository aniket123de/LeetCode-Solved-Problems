class Solution:
    def countSeniors(self, details: list[str]) -> int:
        count = 0
        for word in details:
            age = int(word[11:13])
            if age > 60:
                count += 1           
        return count
