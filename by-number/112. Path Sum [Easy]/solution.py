# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(r, t, runningSum=0):
            if r == None:
                return False
            
            if r.left == None and r.right == None:
                return r.val + runningSum == t
            
            curSum = runningSum + r.val
            
            return dfs(r.left, t, curSum) or dfs(r.right, t, curSum)
        
        return dfs(root, targetSum, 0)


# Submission:
# Time: 38ms - 79.10%
# Space: 17.5mb - 66.72%
# Runtime: