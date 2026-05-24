class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucketList = [[] for _ in range(len(nums) + 1)]
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        for key in freq:
            bucketList[freq[key]].append(key)

        count = 0
        res = []
        for i in range(len(bucketList)-1,-1,-1):
            #print(bucketList,count, k)
           
            if len(bucketList[i]) > 0:
                for num in bucketList[i]:
                    if count < k:
                        res.append(num)
                        count += 1
                    else:
                        return res

        return res

