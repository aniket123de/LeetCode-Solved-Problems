class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            partner = mid ^ 1
            if nums[mid] == nums[partner]:
                low = mid + 1
            else:
                high = mid
        return nums[low]