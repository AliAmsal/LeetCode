class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = ""
        m = len(strs[0])
        for i in range(len(strs)):
            m = min(m,len(strs[i]))
        ans = 0
        for i in range(1,m+1):
            ans = i
            f = True
            for j in range(len(strs)-1):
                if strs[j][:i] == strs[j+1][:i]:
                    continue
                return strs[0][:i-1]
        return strs[0][:ans]
            