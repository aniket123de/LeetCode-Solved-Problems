class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            snum = str(num)
            length = len(snum)
            if length % 2 == 0:
                count += 1

        return count