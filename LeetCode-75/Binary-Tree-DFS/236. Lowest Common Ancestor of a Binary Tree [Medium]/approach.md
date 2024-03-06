What is being asked here?

We are given a binary tree. We are also given two nodes P and Q.
The tree will never be empty.
P and Q will always be in the tree.

The goal is to find the earlist node that both P and Q share. P or Q can be their own earliest node if the other is a descendant of that node.

So how do we approach this?
Well how would I solve this as a human? I would probably go through every node starting fro the root to see which paths lead to nodes P and Q. When we reach P or Q, we can assign those to soe arrays of nodes. If we were looking for 5 and 7, we could get the paths of [1, 3, 5], [1, 3, 4, 7]

Then i guess we could just iterate through each array until we found the first common node alue they share?