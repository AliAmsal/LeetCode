class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        arr = []
        '''
        for val in nums:
            if not val in arr:
                arr.append(val)
        '''
        ans = []
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[j] - nums[i] > k:
                    break
                if nums[j] - nums[i] == k:
                    ans.append(str(nums[i]) + str(nums[j]))
        print(ans)
        for val in ans:
            if not val in arr:
                arr.append(val)
        return len(arr)
    
        