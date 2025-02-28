import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # A min-heap always has its smallest element at the root.
        min_heap = []
        for n in nums:
            heapq.heappush(min_heap, n)
            # Keeping Only k Elements
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return min_heap[0]
