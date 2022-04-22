class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x = str(x)
            x = x[1:]
            ans = ""
            for c in x:
                ans = c + ans
            ans = int(ans)
            if ans > 2**31:
                return 0
            return ans*-1
        
        x = str(x)
        ans = ""
        for c in x:
            ans = c + ans
        ans = int(ans)
        if ans > 2**31-1:
            return 0
        return ans