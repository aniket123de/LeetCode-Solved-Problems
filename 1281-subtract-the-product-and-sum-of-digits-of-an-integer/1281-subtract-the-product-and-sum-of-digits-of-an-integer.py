class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        pdt, add = 1, 0
        result = 0
        s = str(n)
        for char in s:
            pdt *= int(char)
            add += int(char)
        result = pdt - add
        return result