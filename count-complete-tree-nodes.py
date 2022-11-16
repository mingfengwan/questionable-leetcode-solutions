# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def compute_depth(self, node: TreeNode) -> int:
        """
        Return tree depth in O(d) time.
        """
        d = 0
        while node.left:
            node = node.left
            d += 1
        return d

    def compute_right_depth(self, node: TreeNode) -> int:
        """
        Return the depth of the right most node in O(d) time.
        """
        d = 0
        while node.right:
            node = node.right
            d += 1
        return d
        
    def countNodes(self, root: TreeNode) -> int:
        # if the tree is empty
        if not root:
            return 0
        
        d = self.compute_depth(root)
        
        # A maxium of 2**d nodes possible in the last level
        nodes = 2**d
        start = root
        max_d = d - 1
        while max_d >= 0:
            if start.left is None:
                nodes -= 2
            elif self.compute_right_depth(start.left) == max_d:
                if not start.right:
                    nodes -= 1
                else:
                    start = start.right
            else:
                start = start.left
                nodes -= 2**max_d
            max_d -= 1
        
        # The tree contains 2**d - 1 nodes on the first (d - 1) levels
        # plus the nodes in the last level.
        return (2**d - 1) + nodes
