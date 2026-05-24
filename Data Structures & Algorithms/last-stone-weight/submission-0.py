import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        for stone in stones:
            heapq.heappush(heap, -1*stone)
        
        while len(heap) > 1:
            print(heap)
            heavy1 = -1 * heapq.heappop(heap)
            heavy2 = -1 * heapq.heappop(heap)

            if heavy1 == heavy2:
                # destroy
                continue
            if heavy1 > heavy2:
                heapq.heappush(heap, -1*(heavy1-heavy2))
            
        
        if len(heap) == 1:
            return -1*heap[0]
        else:
            return 0
            



        