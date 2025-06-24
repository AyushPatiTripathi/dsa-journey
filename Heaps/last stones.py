import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]
            heapq.heapify(stones)
            
        while len(stones) >1 :

            y  = heapq.heappop(stones)
            x = heapq.heappop(stones)
            if x != y :
                heapq.heappush(stones ,y-x)
        if len(stones) == 1:
            return -heapq.heappop(stones) 
        else :
            return 0
        
       
