# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        que = [root]
        res = []
        
        if root == None:
            return res
        
        while que:
            # Add the right most value of the current level
            res.append(que[-1].val)
            
            # Prepare an empty list for the next level
            nextLevel = []
            
            # Add each node in the next level
            for node in que:
                if node.left != None:
                    nextLevel.append(node.left)
                
                if node.right != None:
                    nextLevel.append(node.right)
        
            # the que is now the next level in the tree
            que = nextLevel
        
        return res


# Submission:
# Time: 42ms - 19.39%
# Space: 16.5mb - 52.05%
# Runtime: