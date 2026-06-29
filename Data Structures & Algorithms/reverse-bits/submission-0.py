class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0

        for i in range(32):
            bit = n % 2

            ans = ans * 2 + bit

            n = n // 2

        return ans