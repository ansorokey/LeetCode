# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # create a recursive helper function
        # takes in a node/root and a reference to a list
        def recur(node, seq):
            # the current node only gets added to the list if it is a leaf
            if node.left == None and node.right == None:
                seq.append(str(node.val))
            
            # check left child
            if node.left:
                recur(node.left, seq)
                
            # check right child
            if node.right:
                recur(node.right, seq)
                
        # create the lists to modify
        seq1, seq2 = [], []

        # run through
        recur(root1, seq1)
        recur(root2, seq2)
        
        # join lists and compare as strings
        # use any character as a separator to avoid '71' = '7 1'
        return '-'.join(seq1) == '-'.join(seq2)


# Submission:
# Time: 34ms - 76.68%
# Space: 16.6mb - 87.52%
# Runtime: O(a + b)