class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if we're given an empty root, then there is no depth
        if root == None:
            return 0
            
        # if we DO have a root, then we also have children
        # The length is this node (1) plus the depth of the child
        leftMax = self.maxDepth(root.left)+1
        rightMax = self.maxDepth(root.right)+1

        # return the biggest one
        return max(rightMax, leftMax)


# Submission:
# Time: 49ms - 14.31%
# Space: 17.6mb - 71.93%
# Runtime: O(n)