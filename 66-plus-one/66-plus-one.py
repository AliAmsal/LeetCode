class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        arr = [9]*len(digits)
        if arr == digits:
            return [1] + [0]*len(digits)
        for i in range(len(digits)-1,-1,-1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0