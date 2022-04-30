class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ""
        for c in s:
            if ord(c) >= 97 and ord(c) <= 122 or ord(c) >= 48 and ord(c) <= 57:
                st += c
            elif ord(c) >= 65 and ord(c) <= 90:
                st += c.lower()
        #if len(st) == 0:
        #    return False
        return st == st[::-1]