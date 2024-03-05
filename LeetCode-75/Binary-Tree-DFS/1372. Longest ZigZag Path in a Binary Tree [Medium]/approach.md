We are given a root node.

Our task is to find the longest ZIGZAG path in the tree. A path is considered zigzag if it goes from left to right or from right to left.
This means it must go in the opposite direction from the parent.
We must also keep in mind that the longest path may not originate from the root node. Meaning the longest path can start from any node, meaning that at any node, we need to be tracking future length.

So a unique dfs must be performed at EACH node.