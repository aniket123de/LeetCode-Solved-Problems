class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        pos, neg, zero = 0, 0, 0
        for num in nums:
            if num < 0:
                neg += 1
            elif num > 0:
                pos += 1
            else:
                zero += 1
        return max(pos, neg)