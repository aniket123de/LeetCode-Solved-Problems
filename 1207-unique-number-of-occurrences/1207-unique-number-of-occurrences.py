class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        arr2 = []
        count_dict = {}
        for num in arr:
            if num in count_dict:
                count_dict[num] += 1
            else:
                count_dict[num] = 1
        arr2 = count_dict.values()
        if len(arr2) == len(set(arr2)):
            return True
        else:
            return False