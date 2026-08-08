class Solution:
    def minBitFlips(self, x: int, y: int) -> int:
        binx = bin(x)[2:]
        biny = bin(y)[2:]
        count = 0
        maxlen = max(len(binx), len(biny))
        binxp = binx.zfill(maxlen)
        binyp = biny.zfill(maxlen)

        bx = list(binxp)
        by = list(binyp)

        for n1, n2 in zip(bx, by):
            if int(n1) ^ int(n2) != 0:
                count += 1
        return count