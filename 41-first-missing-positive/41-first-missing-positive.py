class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        d = {}
        for v in nums:
            if v < 0:
                continue
            d[v] = 0
        ans = 1
        while True:
            if ans in d:
                ans += 1 
                continue
            return ans
        