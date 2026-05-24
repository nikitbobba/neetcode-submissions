class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in store:
                return [store[remainder], i]
            
            store[nums[i]] = i
        
        return []
        