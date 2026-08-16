class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numset = set(nums)
        if len(nums) == len(numset):
            return False
        else:
            return True