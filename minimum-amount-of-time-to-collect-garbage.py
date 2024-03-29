class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        G = P = M = False
        ans = len(garbage[0])

        for i in range(len(travel), 0, -1):
            G |= 'G' in garbage[i]
            P |= 'P' in garbage[i]
            M |= 'M' in garbage[i]
            ans += travel[i-1] * (G + P + M) + len(garbage[i])
        
        return ans
