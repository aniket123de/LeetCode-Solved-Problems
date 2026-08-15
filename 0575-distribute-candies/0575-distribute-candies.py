class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n = len(candyType)
        s = len(set(candyType))
        result = min(n//2, s)
        return result