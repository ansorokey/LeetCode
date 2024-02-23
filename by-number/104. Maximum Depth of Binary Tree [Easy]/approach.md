What is being asked here?

We need to find the path that has the longest number of nodes in it.
This mean we start from the root and look at each child node.
Add the child nodes.
Add those childs node, etc.
Continue this until we reach a null node. At that point, we can start returning a depth. This would probbaly be done best with recursion.