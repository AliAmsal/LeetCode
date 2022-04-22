class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)-1):
            c = 0
            
            if nums[i] == '_':
                break
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    c += 1
                else:
                    break
            count = count + c
            for k in range(c):
                nums.remove(nums[i+1])
                nums.append('_')
                print("here")
                
        print(count)
        return len(nums) - count