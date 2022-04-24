from itertools import permutations  
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]: 
        print ("All the permutations of the given list is:")   
        return list(permutations(nums, len(nums))) 