# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # keep track of node values at their indices
        values = []

        # iterate through nodes
        cur = head
        while cur != None:
            values.append(cur.val)
            cur = cur.next
        
        # lowest possible value to compare to
        maxSum = float('-inf')
        for i in range(len(values)//2):
            # grab the pair values
            a = values[i]
            b = values[len(values) - i - 1]
            
            # compare and set
            if a+b > maxSum:
                maxSum = a+b
                
        return maxSum


# Submission:
# Time: 370ms - 38.96%
# Space: 44.6mb - 38.04%
# Runtime: O(n)