# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.longest = 0
        
        def dfs(node, curLen=0, last='n', nex='n', first=False):
            if node == None:
                return
            
            if last != nex:
                curLen += 1
                if curLen > self.longest:
                    self.longest = curLen                
            else:
                curLen = 1
                if first:
                    curLen = 0
                     
            dfs(node.left, curLen, last=nex, nex='l')
            dfs(node.right, curLen, last=nex, nex='r')
            
        dfs(root, first=True)
        
        return self.longest


# Submission:
# Time: 175ms - 81.71%
# Space: 31.2mb - 28.18%
# Runtime: