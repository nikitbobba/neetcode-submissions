class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            # first place the prefix in the output array at this position
            res[i] = prefix
            # now update the prefix val to what it should be next
            prefix *= nums[i]
        suffix = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= suffix
            suffix *= nums[i]
        return res
        