# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        res = {
            'count': 0
        }
        
        def dfs(node, prevSums=[]):
            if node == None:
                return
            
            for i in range(len(prevSums)):
                prevSums[i] += node.val
                if prevSums[i] == targetSum:
                    res['count'] += 1
                    
            if node.val == targetSum:
                res['count'] += 1

            dfs(node.left, prevSums + [node.val]) 
            dfs(node.right, prevSums + [node.val])
                    
        
        dfs(root)
        
        return res['count']


# Submission:
# Time: 245ms - 38.83%
# Space: 43.8mb - 7.87%
# Runtime:
# NEED COMMENTS