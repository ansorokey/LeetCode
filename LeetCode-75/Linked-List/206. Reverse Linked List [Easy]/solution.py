# Iteration
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if head == None:
#             return None
        
#         cur = head
#         prev = None
        
#         while cur != None:
#             nextNode = cur.next
#             cur.next = prev
#             prev = cur
            
#             cur = nextNode
            
#         # Our cur pointer should be null,
#         # Which means the node before it is the last in the list, the new head
#         return prev


# Submission:
# Time: 36ms - 71.10%
# Space: 17.7mb - 63.74%
# Runtime: O(n)

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # recursive helper function
        def _reverseList(head, prev=None):
            if head.next == None:
                head.next = prev
                global newHead
                newHead = head
                return head
            
            newNode = _reverseList(head=head.next, prev=head)
            head.next = prev
            return newNode
        
        
        if head == None:
            return None
        
        return _reverseList(head)

# Submission:
# Time: 42ms - 30.89%
# Space: 17.7mb - 87.57%
# Runtime: O(n)