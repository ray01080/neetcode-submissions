class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        heap = [(round((x[0]**2+x[1]**2)**0.5,3),i) for i,x in enumerate(points)]
        heapq.heapify(heap)
        # print(heap)
        for n in range(k):
            min_,min_i = heapq.heappop(heap)
            res.append(points[min_i])
        return res