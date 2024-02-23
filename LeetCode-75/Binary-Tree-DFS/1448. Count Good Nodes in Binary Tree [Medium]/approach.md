So what is being asked here?

We are gien a binary tree. Our goal is to count the number of GOOD nodes an return that number.
Any node is good as long as any node in the path before it is not larger than this node's value.

For exaple, if we were given a root of just 3, it would be 1 good node.
In that path [3], there is no value larger than 3.

If we were given 
  3
1  4

We would have two good nodes.
[3, 1] 3 is greater than 1,
and in [3, 4] 4 is greater than 3

So it looks like in any given path to a node, we need to keep track of the highest value in that current path. If the current node is equal to or grater than the higest path node, we can increment the count. Otherwise, we move on.

This sounds like a depth first search.
Along with passing nodes, we should also pass maxValues on.