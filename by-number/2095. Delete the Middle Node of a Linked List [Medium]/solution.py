class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteMiddle(self, head):
    """
    :type head: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    # create a counter for the length of the linked list, 1 indexed
    length = 0

    # assign a pointer to start at the head
    cur = head

    # move through the linked list and incrememnt the length
    while cur != None:
        length += 1
        # advance the pointer
        cur = cur.next

    # edge case, we want to remove a node when there's only one node
    if length == 1:
        return None

    # the 0-index node we want to remove
    target = length // 2

    # reassign a pointer to begin at the front
    cur = head
    # assign a pointer to keep track of the last node
    prev = None
    # track the curent 0-index position
    index = 0

    # iterate through linked list
    while cur != None:
        # if we found the node to remove,
        # have the previous node skip over this one, and point to the next
        if index == target:
            if prev != None:
                prev.next = cur.next
            cur = None
        else:
            # otherwise, advance everything forwards
            prev = cur
            cur = cur.next
            index += 1

    # the current linked list from the head now skips one node
    return head



# Submission:
# Time: 1741ms - 70.10%
# Space:96.7mb -56.64%
# Runtime: O(n)
