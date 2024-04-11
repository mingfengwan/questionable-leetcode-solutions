class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def update_bitmasks(i, j, digit):
            b = calculate_box_index(i, j)
            num = 1 << (digit - 1)
            rows[i] |= num
            cols[j] |= num
            boxes[b] |= num
        
        def calculate_box_index(i, j):
            return (i // 3) * 3 + (j // 3)

        def backtrack(i, j):
            if board[i][j] != ".":
                if i == j == 8:
                    return True
                if i < 8:
                    return backtrack(i + 1, j)
                else:
                    return backtrack(0, j + 1)
                        
            for d in range(9):
                b = calculate_box_index(i, j)
                num = 1 << d
                if num & (rows[i] | cols[j] | boxes[b]):
                    continue
                update_bitmasks(i, j, d + 1)
                board[i][j] = str(d + 1)
                if i == j == 8:
                    return True
                if i < 8:
                    if backtrack(i + 1, j):
                        return True
                else:
                    if backtrack(0, j + 1):
                        return True
                
                board[i][j] = "."
                rows[i] ^= num
                cols[j] ^= num
                boxes[b] ^= num
            
            return False
        
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                update_bitmasks(i, j, int(board[i][j]))

        backtrack(0, 0)
