# Questionable LeetCode Solutions
LeetCode Solutions that I believe to be sub-optimal. This repository is incomplete and subject to change (whenever I have time)

## Count number of nodes in a complete Binary Tree
- [LeetCode link](https://leetcode.com/problems/count-complete-tree-nodes/)
- [My solution](https://github.com/mingfengwan/questionable-leetcode-solutions/blob/main/count-complete-tree-nodes.py)

### My approach
After getting the depth of the tree d, we want to know where does the incomplete subtree starts from. For this, we check if the left subtree is "complete". If it is complete, we check for the left subtree of the right subtree. Else, we check for the left subtree of the left subtree.

Thought my solution is still O(log^2(n)) with space O(1), the total runtime time is actually cut in half, since we decrease the depth each time we perform a subtree check.
