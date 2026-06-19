class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow_helper(base, exp):
            if exp == 0:
                return 1

            half = pow_helper(base, exp // 2)

            if exp % 2 == 0:
                return half * half
            else:
                return half * half * base

        if n < 0:
            n = -n
            x = 1/x

        return pow_helper(x, n)
        