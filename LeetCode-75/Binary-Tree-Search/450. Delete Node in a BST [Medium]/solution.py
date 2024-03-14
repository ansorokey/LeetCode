"""
Non functional solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def findNodeAndParent(node, parent=None):
            if node == None:
                return [None, None]
            
            if node.val == key:
                return [node, parent]
            
            res = [None, None]
            if node.val > key:
                res =findNodeAndParent(node.left, node)
            else:
                res = findNodeAndParent(node.right, node)
                
            return res
        ###################################################
        
        [dnode, parentNode] = findNodeAndParent(root)
        
        # Never found a matching node value, return tree as is
        if dnode == None:
            return root
        
        #Edge Case: node to delete was root, only node in tree
        if dnode == root and not node.left and not node.right:
            return None
        
        # Case 1: The node has no children
        if dnode.left == None and dnode.right == None:
            return root
        
        # Case 2: The node has ONE child
        if parentNode.left == dnode:
            #Attach to the parent's left
            if dnode.left and not dnode.right:
                parentNode.left = dnode.left
            elif dnode.right and not dnode.left:
                parentNode.left = dnode.right
        else:
            #Attach to the parents right
            if node.left and not dnode.right:
                parentNode.right = dnode.left
            elif dnode.right and not dnode.left:
                parentNode.right = dnode.right
            
        #  Case 2: node has two children
            
        return root

"""

#  Working solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # Null root? return null
        if root == None:
            return None

        # COMPARING VALUES
        # Is the key we're looking for less than the curent value?
        if key < root.val:
            # go left
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            # Larger? Go right
            root.right = self.deleteNode(root.right, key)
        else:
            # Found the value
            # if the node is missing a child, then the other 
            # child is instantly the next node in line
            if root.left == None:
                return root.right
            elif root.right == None:
                return root.left
            else:
                # find the smallest value of the greater side of this root's tree
                # Move to the right
                cur = root.right
                
                # Find the last valid left side node
                while cur.left:
                    cur = cur.left

                # give the current root this value
                root.val = cur.val

                # now go and delete the node we took the value from
                root.right = self.deleteNode(root.right, root.val)
        return root


# Submission:
# Time:
# Space:
# Runtime: