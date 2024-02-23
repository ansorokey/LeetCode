def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # a head and pointer to trak odd indicies
    oddHead = ListNode()
    lastOdd = oddHead
    
    # a head and pointer to track even indices
    evenHead = ListNode()
    lastEven = evenHead
    
    # a pointer to iterate list
    cur = head
    # a boolean to track if even or odd
    isEven = False
    
    while cur != None:
        # move the proper pointer forward
        if isEven:
            lastEven.next = cur
            lastEven = cur
        else:
            lastOdd.next = cur
            lastOdd = cur
            
        # inverse boolean for next node
        isEven = not isEven
        
        # advance pointer
        cur = cur.next
        
    # clean up the end of the list to avoid a cycle
    lastEven.next = None

    # connext the start of the evens to the end of the odds
    lastOdd.next = evenHead.next
    
    # return the start of the odds
    return oddHead.next


# Submission:
# Time: 36ms - 81.76%
# Space: 18.7mb - 58.18%
# Runtime: O(n) time, O(1) space