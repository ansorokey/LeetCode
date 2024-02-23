# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Helper dfs function
        def dfs(root, maxVal, goodNodes):
            if root == None:
                return 

            # if current value is greater than or equal to path max
            if root.val >= maxVal:
                goodNodes.append(root.val)
                maxVal = root.val

            dfs(root.left, maxVal, goodNodes)
            dfs(root.right, maxVal, goodNodes)
                
        goodNodes = []
        dfs(root, root.val, goodNodes)
        
        return len(goodNodes)


# Submission:
# Time: 137ms - 51.35%
# Space: 31.4mb - 56.25%
# Runtime: O(n) time and O(n) space


# Uses a simler count variable, no list to append to
        def dfs(root, maxVal):
            count = 0
            if root == None:
                return 0

            # if current value is greater than or equal to path max
            if root.val >= maxVal:
                maxVal = root.val
                count += 1

            count += dfs(root.left, maxVal)
            count += dfs(root.right, maxVal)
                
            return count
        
        return dfs(root, root.val)

# Submission:
# Time: 132ms - 63.54%
# Space: 31.4mb - 56.25%
# Runtime: O(n) time and O(n) space