class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0

        for n in numSet:
            if n - 1 in numSet:
                # this is an ongoing sequence, skip
                continue
            else:
                tmp = 1 # include this num
                while n+tmp in numSet:
                    tmp += 1
                res = max(res, tmp)
        
        return res
        