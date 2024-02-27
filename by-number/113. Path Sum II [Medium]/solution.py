# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # The lists of all paths hat sum to target
        res = []
        
        # return early for null initial root
        if root == None:
            return res
        
        # define helper function
        def dfs(node, path=[], runningSum=0):
            curPath = path + [node.val]
            runningSum += node.val
            
            # reaching a leaf node
            if node.left == None and node.right == None:
                # only add the path if the sum matches
                if runningSum == targetSum:
                    res.append(curPath)
                return
            
            if node.left:
                dfs(node.left, curPath, runningSum)
                
            if node.right:
                dfs(node.right, curPath, runningSum)
            
        dfs(root)
        
        return res


# Submission:
# Time:
# Space:
# Runtime: