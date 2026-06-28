class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result_array = []
        hashMap = {}
        for i, n in enumerate(nums):
            if n in hashMap:
                hashMap[n] += 1
            else:
                hashMap[n] = 1
        
        while k > 0:
            max_key = max(hashMap, key=hashMap.get)
            result_array.append(max_key)
            largest_value = hashMap.pop(max_key)
            k -= 1
    
        return result_array
        