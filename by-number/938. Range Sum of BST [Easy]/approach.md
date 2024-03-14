We are given a binary search tree, which is already sorted, and an INCLUSIVE range, meaning the values CAN match.

The goal is to return a sum of all nodes that are within that range.

Now the most brute force approach would be to go through each and every node, compare the value to the range, and sum a running total to return. Let's do that with a DFS.