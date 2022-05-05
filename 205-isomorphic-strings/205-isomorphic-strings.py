class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d = {}
        ans = ""
        for i in range(len(s)):
            if s[i] in d:
                ans += d[s[i]]
            else:
                d[s[i]] = t[i]
                ans += d[s[i]]
        if ans == t:
            ans = ""
            d = {}
            for i in range(len(s)):
                if t[i] in d:
                    ans += d[t[i]]
                else:
                    d[t[i]] = s[i]
                    ans += d[t[i]]
            return ans == s
        else:
            return False