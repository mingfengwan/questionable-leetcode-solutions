class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 26

        for i in range(len(s)):
            curr = ord(s[i]) - ord('a')
            current_max = dp[curr]

            for c in range(max(0, curr - k), min(26, curr + k + 1)):
                current_max = max(current_max, dp[c])
            
            dp[curr] = current_max + 1
        
        return max(dp)
