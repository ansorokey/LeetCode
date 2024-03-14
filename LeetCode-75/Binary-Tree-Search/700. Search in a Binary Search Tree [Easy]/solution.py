# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        stack = [root]
        
        while stack:
            cur = stack.pop()
            
            if cur == None:
                return None
            
            if cur.val == val:
                return cur
            elif val < cur.val:
                stack.append(cur.left)
            else:
                stack.append(cur.right)
                
        return None


# Submission:
# Time: 58ms - 40.33%
# Space: 18.4mb - 38.58%
# Runtime:

# WITHOUT STACK
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        cur = root
        
        while cur:
            if cur == None:
                return None
            
            if cur.val == val:
                return cur
            elif val < cur.val:
                cur = cur.left
            else:
                cur = cur.right
                
        return None

# Submission:
# Time: 61ms - 22.23%
# Space: 18.3mb - 85.64%
# Runtime:

# EVEN FASTERERRRRRRR

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root:
            if root == None:
                return None
            
            if root.val == val:
                return root
            elif val < root.val:
                root = root.left
            else:
                root = root.right
                
        return None

# Submission:
# Time: 53ms - 73.14%
# Space: 18.2mb - 85.64%
# Runtime: