class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashMap = {}

        for num in nums:
            if hashMap.get(num):
                return True
            hashMap[num] = True
            
        return False
        