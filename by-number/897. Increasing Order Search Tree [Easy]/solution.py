# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        newNode = TreeNode()
        self.cur = newNode
        
        def dfs(node):
            if node == None:
                return
                
            dfs(node.left)
            print(node.val, self.cur)
            self.cur.right = TreeNode(node.val)
            self.cur = self.cur.right
            dfs(node.right)
            
        dfs(root)
        return newNode.right

# Submission:
# Time: 43ms - 10.60%
# Space: 16.5mb - 52.46%
# Runtime:

# Better solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        # This will be the new head of the rearranged tree
        newNode = TreeNode()
        self.cur = newNode
        
        def dfs(node):
            # do nothing at a null node
            if node == None:
                return
                
            # Go as left as we can
            dfs(node.left)
            # set the right pointer of our pointer node to current node
            self.cur.right = node

            # advance the pointer node
            self.cur = self.cur.right

            # clear current node's left side
            node.left = None

            # repeat on the right
            dfs(node.right)
            
        dfs(root)
        return newNode.right

# Submission:
# Time: 33ms - 78.11%
# Space: 16.5mb - 94.94%
# Runtime: