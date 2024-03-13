# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        minLevel = 1
        depth = 1
        maxSum = float('-inf')
        que = [root]
        
        while que:
            nextLevel = []
            curSum = 0
            
            for node in que:
                curSum += node.val
                
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
                
            if curSum > maxSum:
                maxSum = curSum
                minLevel = depth
                
            depth += 1
            que = nextLevel
            
        return minLevel


# Submission:
# Time: 139ms - 96.55%
# Space: 19.8mb - 98.24%
# Runtime: