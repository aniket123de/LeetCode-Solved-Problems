class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        starting = set()
        for arr in paths:
            starting.add(arr[0])
        for arr in  paths:
            dest = arr[1]
            if dest not in starting:
                return dest