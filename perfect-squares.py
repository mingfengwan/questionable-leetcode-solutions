class Solution:
    def isSquare(self, n: int) -> bool:
        return math.sqrt(n).is_integer()

    def numSquares(self, n: int) -> int:
        # four-square and three-square theorems
        while (n & 3) == 0:
            n >>= 2      # reducing the 4^k factor from number
        if (n & 7) == 7: # mod 8
            return 4

        if self.isSquare(n):
            return 1
        # check if the number can be decomposed into sum of two squares
        for i in range(int(n**(0.5)), int((n/2)**(0.5)) - 1, -1):
            if self.isSquare(n - i*i):
                return 2
        # bottom case from the three-square theorem
        return 3
