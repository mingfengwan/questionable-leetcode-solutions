# Questionable LeetCode Solutions
LeetCode Solutions that I believe to be sub-optimal.

## Minimum Amount of Time to Collect Garbage
### `✅ Accepted as official solution`
- [LeetCode link](https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/)
- [My solution](https://github.com/mingfengwan/questionable-leetcode-solutions/blob/main/minimum-amount-of-time-to-collect-garbage.py)
- [LeetCode Repo Issue](https://github.com/LeetCode-Feedback/LeetCode-Feedback/issues/18275)

### My approach
No need for extra space or modifying the array input in-place. Just loop backward.

## Sudoku Solver
### `✅ Accepted as official solution`
- [LeetCode link](https://leetcode.com/problems/sudoku-solver/)
- [My solution](https://github.com/mingfengwan/questionable-leetcode-solutions/blob/main/sudoku-solver.py)
- [LeetCode Repo Issue](https://github.com/LeetCode-Feedback/LeetCode-Feedback/issues/21793)

### My approach
Bitmasking instead of hash set. Hash set consumes 9 times more space than bitmasking ($O(n^2)$ versus $O(n)$).

## Count number of nodes in a complete Binary Tree
- [LeetCode link](https://leetcode.com/problems/count-complete-tree-nodes/)
- [My solution](https://github.com/mingfengwan/questionable-leetcode-solutions/blob/main/count-complete-tree-nodes.py)

### My approach
After getting the depth of the tree d, we want to know where the incomplete subtree starts from. For this, we check if the left subtree is "complete". If it is complete, we check for the left subtree of the right subtree. Else, we check for the left subtree of the left subtree.

Though my solution is still $O(log^2(n))$ with space $O(1)$, the total runtime time is actually cut in half since we decrease the depth each time we perform a subtree check.

## Perfect squares
- [LeetCode link](https://leetcode.com/problems/perfect-squares/)
- [My solution](https://github.com/mingfengwan/questionable-leetcode-solutions/blob/main/perfect-squares.py)

### My approach
Similar to the official solution, but there's no need to loop from $\lfloor\sqrt{n}\rfloor$ to $1$ to check if the number can be decomposed into sum of two squares. Instead we only need to loop from $\lfloor\sqrt{n}\rfloor$ to $\lfloor\sqrt{0.5n}\rfloor$.

## 3Sum Smaller
- [LeetCode link](https://leetcode.com/problems/3sum-smaller/)
- [My solution](https://github.com/mingfengwan/questionable-leetcode-solutions/blob/main/3sum-smaller.py)

### My approach
Instead of checking the pairs of $(j,k)$ one by one, for every pair of $(i,j)$ we decrement $k$ from `len(nums) - 1`. If `nums[i] + nums[j] + nums[k] < target`, we break the while loop and increment the total number of pairs by $k-j$.

## 24 Game
- [LeetCode link](https://leetcode.com/problems/24-game/)
- [My solution](https://github.com/mingfengwan/questionable-leetcode-solutions/blob/main/24-game.py)

### My approach
The code is a lot faster if we set base case to be array size equal to $2$ instead of $1$.

## Set Matrix Zeroes
- [LeetCode link](https://leetcode.com/problems/set-matrix-zeroes/)
- [My solution](https://github.com/mingfengwan/questionable-leetcode-solutions/blob/main/set-matrix-zeroes.py)

### My approach
One less for loop compared to the official solution.

## Longest Ideal Subsequence
- [LeetCode link](https://leetcode.com/problems/longest-ideal-subsequence/)
- [My solution](https://github.com/mingfengwan/questionable-leetcode-solutions/blob/main/longest-ideal-subsequence.py)

### My approach
There are several redundancies in the solution. Looping through all 26 characters is unnecessary.
