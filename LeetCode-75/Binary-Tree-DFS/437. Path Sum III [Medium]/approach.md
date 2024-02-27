What is being asked here?

We are given a binary tree and an integer sum.
The goal is to return the number of paths that add to that sum.

The trick here is that the sum can start and end anywhere. It can be in the middle of the tree, for example.
So that means that at any point in the tree, if this node plus the children node of one path equal the target, a count goes up.

So we should make a recursive dfs helper.

Alright, we've come back after a little break.
After solving path sum 1 an 2, I've come to a different idea.
The trouble I was originall having with this problem is how to start a new sum with each child node, that way a path could be found in the middle of a tree. This means a variable number of running sums. I was trying to solve this with only one running sum, where I should maybe be keeping track of all previous running sums up until the current node, and creating a new one with the next traversal. Then, at each node, I should be iterating through the given sums and test if that previous sum plus current value is equal to the target, and increment a global counter.