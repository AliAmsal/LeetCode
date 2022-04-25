class Solution:
    def maxArea(self, height: List[int]) -> int:
        m = 0
        #for i in range(len(height)-1):
         #   for j in range(1,len(height)):
          #      m = max(m,(j-i)*min(height[i],height[j]))
        
        i = 0
        j = len(height) - 1
        while (i != j):
            m = max(m,(j-i)*min(height[i],height[j]))
            if height[i] >= height[j]:
                j -= 1
            else:
                i += 1
        return m