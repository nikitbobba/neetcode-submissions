class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque() # going to store indices

        l = r = 0

        while r < len(nums):
            #print(q)
            while q and nums[r] > nums[q[-1]]:
                # remove the  numbers at the end of 
                # the queue that are smaller than the
                # current value at r
                q.pop()
            
            q.append(r)

            if (r-l+1) == k:
                res.append(nums[q[0]]) # max val will always be at front of queue
                l += 1
            
            r += 1

            if l > q[0]:
                q.popleft()
        return res
        