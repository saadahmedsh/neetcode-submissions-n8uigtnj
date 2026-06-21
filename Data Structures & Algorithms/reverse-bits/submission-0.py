class Solution:
    def reverseBits(self, n: int) -> int:

        print(1 << 0)
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            mask = (bit << (31 - i))
            res += mask

        return res