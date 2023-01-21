# Questionable LeetCode Solutions
LeetCode Solutions that I believe to be sub-optimal. This repository is incomplete and subject to change (whenever I have time)

## Count number of nodes in a complete Binary Tree
- [LeetCode link](https://leetcode.com/problems/count-complete-tree-nodes/)
- [My solution](https://github.com/mingfengwan/questionable-leetcode-solutions/blob/main/count-complete-tree-nodes.py)

### My approach
After getting the depth of the tree d, we want to know where does the incomplete subtree starts from. For this, we check if the left subtree is "complete". If it is complete, we check for the left subtree of the right subtree. Else, we check for the left subtree of the left subtree.

Thought my solution is still O(log^2(n)) with space O(1), the total runtime time is actually cut in half, since we decrease the depth each time we perform a subtree check.

## Perfect squares
- [LeetCode link](https://leetcode.com/problems/perfect-squares/)
- [My solution](https://github.com/mingfengwan/questionable-leetcode-solutions/blob/main/perfect-squares.py)

### My approach
Similiar to the official solution, but there's no need to loop from floor(n**(0.5)) to 1 to check if the number can be decomposed into sum of two squares. Instead we only need to loop from floor(n**(0.5)) to floor((n/2)**(0.5))

## 3Sum Smaller
- [LeetCode link](https://leetcode.com/problems/3sum-smaller/)
- [My solution](https://github.com/mingfengwan/questionable-leetcode-solutions/blob/main/3sum-smaller.py)

### My approach
Instead of checking the pairs of (j,k) one by one, for every pair of (i,j) we decrement k from len(nums)-1. If nums[i]+nums[j]+nums[k]<target, we break the while loop and increment the total number of pairs by k-j.
