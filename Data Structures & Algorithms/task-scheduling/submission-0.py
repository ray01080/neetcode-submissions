class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = Counter(tasks)
        maxHeap = [-cnt for cnt in cnt.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()# (-cnt, idletime)
        while maxHeap or q:
            time += 1

            if not maxHeap:
                time = q[0][1]
            else:
                ct = 1 + heapq.heappop(maxHeap)
                if ct:
                    q.append([ct, time+n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time