What is being asked here?

Givena linked list, return a new linked list in reversed order. The newly returned head should be the last node in the list, and should point to each node backwards. The first node should point to nothing/null/none.

Im glad we looked at the constaint, because the length of the list can be 0. So our very first step is to check if we have a list at all. If we don't, return nothing/null/none.

Moving on, we know we need to iterate through this linked list. So we need a pointer to the first node/head.
To advance, we set the current node equal to the currents next pointer.
We will also need a pointer that keeps track of the LAST node, that way we can have the node we're about to leave point to that.

Finally, we need to return the new head after all this is done.

Iterative solution works, but how would I go about this recursively?
we would want to call the same function repeatedly. We'd also want to move down the linked list with each call.
So say we get to the last node in the list.
