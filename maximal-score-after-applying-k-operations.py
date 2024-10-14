class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        h = [-x for x in sorted(nums)[-k:]]
        heapq.heapify(h)
        ans = 0

        for _ in range(k):
            val = heapq.heappop(h)
            ans -= val
            heapq.heappush(h, val // 3)
        
        return ans
