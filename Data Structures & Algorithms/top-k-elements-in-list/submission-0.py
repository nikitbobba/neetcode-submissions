class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = count.get(num, 0) + 1

        for num in count.keys():
            freq[count[num]].append(num)

        output = []
        # iterate backwards
        for i in range(len(freq)-1, -1, -1):
            for element in freq[i]:
                if len(output) == k:
                    return output
                
                output.append(element)
        
        return output