class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        arr = []
        n = len(nums)
        for i in range(1,n+1):
            arr.append(i)
        my_dict = dict.fromkeys(arr, 0)

        for num in nums:
            if num in my_dict:
                my_dict[num] += 1
        disapp = []
        for key, value in my_dict.items():
            if value == 0:
                disapp.append(key)
        return disapp