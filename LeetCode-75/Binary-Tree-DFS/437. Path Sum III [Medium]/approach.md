What is being asked here?

We are given a binary tree and an integer sum.
The goal is to return the number of paths that add to that sum.

The trick here is that the sum can start and end anywhere. It can be in the middle of the tree, for example.
So that means that at any point in the tree, if this node plus the children node of one path equal the target, a count goes up.

So we should make a recursive dfs helper.
