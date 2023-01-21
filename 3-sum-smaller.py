class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        total = 0
        n = len(nums)

        for i in range(n - 2):
            for j in range(i+1, n - 1):
                k = n - 1
                while j < k:
                    if nums[i] + nums[j] + nums[k] < target:
                        break
                    k -= 1
                else:
                    break
                total += k - j
        
        return total
