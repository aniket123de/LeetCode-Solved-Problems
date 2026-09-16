class Solution:
    def sumZero(self, n: int) -> list[int]:
        ans = []
        
        # If n is odd, include 0
        if n % 2 != 0:
            ans.append(0)
            
        # Add symmetric pairs (1, -1), (2, -2), ..., (k, -k)
        for i in range(1, (n // 2) + 1):
            ans.append(i)
            ans.append(-i)
            
        return ans