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

## Longest Ideal Subsequence
### `✅ Accepted as official solution`
- [LeetCode link](https://leetcode.com/problems/longest-ideal-subsequence/)
- [My solution](https://github.com/mingfengwan/questionable-leetcode-solutions/blob/main/longest-ideal-subsequence.py)
- [LeetCode Repo Issue](https://github.com/LeetCode-Feedback/LeetCode-Feedback/issues/21962)

### My approach
There are several redundancies in the solution. Looping through all 26 characters is unnecessary.

## Maximal Score After Applying K Operations
### `✅ Accepted as official solution`
- [LeetCode link](https://leetcode.com/problems/maximal-score-after-applying-k-operations/)
- [My solution](https://github.com/mingfengwan/questionable-leetcode-solutions/blob/main/maximal-score-after-applying-k-operations.py)
- [LeetCode Repo Issue](https://github.com/LeetCode-Feedback/LeetCode-Feedback/issues/24776)

### My approach
You only need to gather the largest $k$ elements for the heap. Time complexity reduced to $O(klogk + nlogn)$, space complexity reduced to $O(k)$

## Count Servers that Communicate
### `✅ Accepted as official solution`
- [LeetCode Repo Issue](https://github.com/LeetCode-Feedback/LeetCode-Feedback/issues/26634)

Errors in both the editorial and variable naming.

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

## Grumpy Bookstore Owner
- [LeetCode link](https://leetcode.com/problems/grumpy-bookstore-owner/)
- [My solution](https://github.com/mingfengwan/questionable-leetcode-solutions/blob/main/grumpy-bookstore-owner.py)

### My approach
One less for loop compared to the official solution.

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

## K-th Smallest in Lexicographical Order
- [LeetCode link](https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/)
- [My solution](https://github.com/mingfengwan/questionable-leetcode-solutions/blob/main/k-th-smallest-in-lexicographical-order.py)

### My approach
Using the formula for geometric series instead of a while loop significantly improves the speed of counting the number of steps.

Rationale: Think of this as a permutation problem. For any number between $1$ to $n$, there are $(1 + 10 + 10^2 + \dotsm 10^j) - \max((i + 1) \times 10^j - n - 1 , 0)$ possible numbers starting with $i$, where $j$ is the largest number such that $i\times10^j \leq n$.
