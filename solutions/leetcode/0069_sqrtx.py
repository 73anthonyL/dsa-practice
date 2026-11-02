class Solution:
    def mySqrt(self, x: int) -> int:
        lo, hi = 0, 65536
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if (mid * mid) == x:
                return mid
            elif (mid * mid) < x:
                lo = mid
            else:
                hi = mid - 1

        return lo

        