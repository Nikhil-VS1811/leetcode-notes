# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        Determines if the tree has a root-to-leaf path with sum equal to targetSum.
      
        Args:
            root: Root node of the binary tree
            targetSum: Target sum to find in any root-to-leaf path
          
        Returns:
            True if such a path exists, False otherwise
        """
      
        def dfs(node: Optional[TreeNode], current_sum: int) -> bool:
            """
            Depth-first search helper function to traverse the tree.
          
            Args:
                node: Current node being visited
                current_sum: Sum accumulated from root to current node's parent
              
            Returns:
                True if a valid path is found, False otherwise
            """
            # Base case: empty node
            if node is None:
                return False
          
            # Add current node's value to the running sum
            current_sum += node.val
          
            # Check if we've reached a leaf node with the target sum
            if node.left is None and node.right is None:
                return current_sum == targetSum
          
            # Recursively check left and right subtrees
            # Return True if either subtree contains a valid path
            return dfs(node.left, current_sum) or dfs(node.right, current_sum)
      
        # Start DFS from root with initial sum of 0
        return dfs(root, 0)