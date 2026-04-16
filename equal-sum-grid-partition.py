class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        sums_row = [0] * m
        sums_col = [0] * n

        for i in range(m):
            for j in range(n):
                sums_row[i] += grid[i][j]
                sums_col[j] += grid[i][j]
        
        def can_split_equally(arr, length):
            i = 0
            j = length - 1
            left = arr[i]
            right = arr[j]

            while i < j - 1:
                if left > right:
                    j -= 1
                    right += arr[j]
                else:
                    i += 1
                    left += arr[i]

            return left == right
        
        if m > 1 and can_split_equally(sums_row, m):
            return True

        return n > 1 and can_split_equally(sums_col, n)
