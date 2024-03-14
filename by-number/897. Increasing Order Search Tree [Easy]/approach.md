We are given a binary search tree. We want to transform the tree to that it is one continuous tree of right sided (larger) nodes.

The smallest node in any tree is the left most node. So the first thing we need to do is go all the way to the left.
This is basically an inorder traversal with reassignment.
