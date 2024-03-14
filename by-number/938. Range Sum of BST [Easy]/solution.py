# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node):
            if node == None:
                return 0
            
            curVal = 0
            if node.val >= low and node.val <= high:
                curVal = node.val
            
            return curVal + dfs(node.left) + dfs(node.right)
            
            
        return dfs(root)


# Submission:
# Time: 135ms - 13.94%
# Space: 23.4mb - 99.67%
# Runtime: