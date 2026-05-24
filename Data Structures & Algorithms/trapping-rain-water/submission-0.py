class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0

        L = 0
        R = len(height) - 1

        maxL = height[0]
        maxR = height[len(height)-1]

        while L <= R:
            #print(L, R, maxL, maxR, res)
            if maxL < maxR:
                # process left pointer
                water = maxL- height[L] if (maxL - height[L]) >= 0 else 0
                res += water
                maxL = max(maxL, height[L])
                L += 1
            else:
                # process right pointer
                water = maxR - height[R] if (maxR - height[R]) >= 0 else 0
                res += water
                maxR = max(maxR, height[R])
                R -= 1
            
        return res


        

        
        
        