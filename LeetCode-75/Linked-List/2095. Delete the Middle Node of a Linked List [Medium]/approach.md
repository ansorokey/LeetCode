What is this problem asking us?

We are given the HEAD (first node) of a singly linked list taht is n nodes long.
Our goal is to find the midle nodes of this list, delete it, and return a new linked list without the middle node.
The middle node of a list of length n is considered to be the rounded down floor of the length (n) divided by 2
So a list of length 7 would be 7//2 = 3.5 = node 3 in a 0 indexed list.

Our first goal it to iterate through the linked list. How do we do that? We create an interating variable and assign it to the head.
After we are done doing whatever it is we need to do with that node, we assign the iterating variable (pointer node) to the current nodes's next value.
The list will continue iterating as long as there is a node value there

While we are iterating, we can also keep a count of the index and number of each node.
One can be a length variable sarting at 0
To track indexes, we can keep a map. Actually, thinking about it, we could also just iterate twice.
The second time, we know what nth node to look for, so when we reach it, we can just remove it by asigning the previous value to the next value, like a bridge. let's do that.