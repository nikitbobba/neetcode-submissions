class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxRes = nums[0]

        l = 0
        curr = 0
        for r in range(len(nums)):
            curr += nums[r]
            if curr < 0:
                maxRes = max(maxRes, curr)
                curr = 0
                
            else:
                maxRes = max(maxRes, curr)
        return maxRes
        