class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums)+1)]
        seen = {}
        res = []
        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1
        
        for num in seen:
            f = seen[num]
            freq[f].append(num)
            print(f, freq)
        
        count = 0
        #print(freq)
        print(seen)
        for i in range(len(freq)-1,-1,-1):
            for j in freq[i]:
                if count < k:
                    res.append(j)
                    count += 1
        
        return res



        