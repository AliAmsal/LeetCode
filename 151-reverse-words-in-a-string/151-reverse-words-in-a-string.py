class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        arr = s.split()
        s = ""
        for i in range(len(arr)-1,-1,-1):
            s += arr[i] + " "
        return s[:-1]