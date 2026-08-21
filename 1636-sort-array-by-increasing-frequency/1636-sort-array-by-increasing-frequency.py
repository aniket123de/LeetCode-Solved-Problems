class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        return sorted(nums, key=lambda x: (count[x], -x))
        