import math
class Solution:
    def mySqrt(self, x: int) -> int:
        ans = 1
        while ans**2 <= x:
            ans += 1
        return ans-1