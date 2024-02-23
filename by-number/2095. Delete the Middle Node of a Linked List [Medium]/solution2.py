class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# a single pass, just becasue we can
def deleteMiddle(self, head):
    """
    :type head: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    nodeMap = {
        0: head
    }

    length = 0
    cur = head
    while cur != None:
        nodeMap[length] = cur
        length += 1
        cur = cur.next

    if length == 1:
        return None

    target = length // 2
    nodeMap[target - 1].next = nodeMap[target].next

    return head



# Submission:
# Time: 1741ms - 70.10%
# Space:96.7mb -56.64%
# Runtime: O(n)
