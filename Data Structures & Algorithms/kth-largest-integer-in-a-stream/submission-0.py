class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)
        return None

    def add(self, val: int) -> int:
        res = heapq.heappush(self.heap,val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]