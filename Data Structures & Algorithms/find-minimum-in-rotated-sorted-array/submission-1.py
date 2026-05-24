class Solution:
    def findMin(self, nums: List[int]) -> int:
        L = 0
        R = len(nums)-1
        res = nums[0]

        while L <= R:
            if nums[L] < nums[R]:
                res = min(res, nums[L])
                break
            
            mid = (L+R)//2
            print(mid)
            res = min(res, nums[mid])

            if nums[mid] >= nums[L]:
                # Go right
                L = mid + 1
            else:
                # go left
                R = mid - 1
        return res

            
        