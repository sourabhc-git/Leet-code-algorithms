import heapq
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
        frequency_map = {}
        heap = []

        # Count the frequency of each number
        for num in nums:
            frequency_map[num] = frequency_map.get(num, 0) + 1

        # Push elements into the heap
        for num, freq in frequency_map.items():
            heapq.heappush(heap, (-freq, num))

        # Pop k elements from the heap
        top_k = []
        for _ in range(k):
            top_k.append(heapq.heappop(heap)[1])

        return top_k