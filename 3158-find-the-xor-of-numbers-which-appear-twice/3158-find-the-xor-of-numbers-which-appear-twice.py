class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        count_dict = {}
        for num in nums:
            if num in count_dict:
                count_dict[num] += 1
            else:
                count_dict[num] = 1
        xorlist = []
        for key, value in count_dict.items():
            if value == 2:
                xorlist.append(key)
        result = 0
        for num in xorlist:
            result ^= num
        return result