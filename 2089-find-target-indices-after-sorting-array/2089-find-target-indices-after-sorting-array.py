class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        arr = []
        result = []
        arr = sorted(nums)
        for i in range(len(nums)):
            if arr[i] == target:
                result.append(i)
            i += 1
        return result
