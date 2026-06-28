class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i,num in enumerate(nums):
            if (num in hashMap):
                return [hashMap[num], i]  
                
            diff = target - nums[i] # 6 = 10 - 4
            hashMap[diff] = i # {6: 0}
    
        return None      
        