class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        arr1 = nums[n-k:n]      
        arr2 = nums[0:n-k]     
        nums[:] = arr1 + arr2   