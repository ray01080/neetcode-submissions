class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones)>1:
            y = heapq.heappop_max(stones)
            x = heapq.heappop_max(stones)
            rem = y-x
            if rem != 0:
                heapq.heappush_max(stones,rem)
        return 0 if not stones else stones[0]