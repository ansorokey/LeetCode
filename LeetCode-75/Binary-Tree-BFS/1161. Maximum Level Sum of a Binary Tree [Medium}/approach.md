What is being asked here?

We are given a binary tree.
For each level in the tree (starting at 1 with the root), we want to find the sum of all node values in that level.

Return the FIRST maximum level sum. Assme two level can have the same sum, return the first one only.

Sounds simple enough.
Begin with a breadth first search.
Sum all nodes in the current level.
If the sum is greater than the current maximum sum, replace the level. No need to replace if they're the same.
Add the children to the que for the next level
return the max level at the very end