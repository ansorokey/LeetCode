# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.pPath = []
        self.qPath = []
        
        def dfs(node, path):
            if node == None:
                return
            
            path.append(node)
            
            if node.val == q.val:
                self.qPath = path
                
            if node.val == p.val:
                self.pPath = path
            
            dfs(node.left, [*path])
            dfs(node.right, [*path])
        
        dfs(root, [])

        i, j = len(self.qPath)-1, len(self.pPath)-1
        
        while i >= 0 and j >= 0:
            if self.qPath[i].val == self.pPath[j].val:
                return self.qPath[i]
            if i < j:
                j -= 1
            else:
                i -= 1


# Submission:
# Time: 900ms - 5.00%
# Space: 436.9mb - 5.22%
# Runtime: