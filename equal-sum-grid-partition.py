class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        sums_row = [0] * m
        sums_col = [0] * n
        
        total = 0

        for i in range(m):
            for j in range(n):
                sums_row[i] += grid[i][j]
                sums_col[j] += grid[i][j]
                total += grid[i][j]
        
        if total % 2 != 0:
            return False
        
        half = total // 2
        
        def can_split_equally(arr, length):
            cur = 0

            for i in range(length - 1):
                cur += arr[i]
                if cur == half:
                    return True
                elif cur > half:
                    break

            return False
        
        if can_split_equally(sums_row, m):
            return True

        return can_split_equally(sums_col, n)
