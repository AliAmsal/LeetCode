class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n1 = 0
        n2 = 0
        for i in range(len(a)-1,-1,-1):
            if a[i] == "1":
                n1 += 2**(len(a)-i-1)
        print(n1)
        for i in range(len(b)-1,-1,-1):
            if b[i] == "1":
                n2 += 2**(len(b)-i-1)
        print(n2)
        ans = n1+n2
        return bin(ans)[2:]