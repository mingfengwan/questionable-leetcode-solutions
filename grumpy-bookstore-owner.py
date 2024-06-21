class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        secret_not_used = secret_used = 0

        for i in range(minutes):
            secret_used += customers[i]
        
        ans = secret_used

        for i in range(minutes, len(customers)):
            if not grumpy[i - minutes]:
                secret_not_used += customers[i - minutes]
            secret_used += customers[i]
            secret_used -= customers[i - minutes]
            
            if grumpy[i]:
                ans = max(ans, secret_not_used + secret_used)
            else:
                ans += customers[i]
        
        return ans
