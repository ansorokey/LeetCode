So in this problem, we are give a binary tree. If we are looking at the tree from the right side, we want to return a list of all the visible node values.

Esentially, we want to return the right-most node on each LEVEL of the tree. So in irder to traverse this, we can use a breadth first earch (level by level, top to bottom, left to right)

How do we do a breadth first search? Well, its basically a queue, so we can iterate though a list that starts wth the root node