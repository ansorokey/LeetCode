We are given a biary search tree and an integer.

Return the node that has the same value as the integer.
remember that a binary SEARCH tree is already sorted wth values smaller than the current node on the left and value larger on the right.

So at any given node, we check if it matches the value.
If not, is the value smaller?
Otherwise, it is larger
Move in that direction.