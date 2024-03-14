What do we have to do in this problem?

Given the root of a binary seach tree and a value, find the root that has that value (IF it exists in the tree) and deete that node.
After deleting that node, fix the rest of the tree with its children

So frst off, this can be plit into two parts:
The first part is simply finding the node. Whether we find the node or not, we return the root. What if the root is the thing we need to delete?
Then we have to return the new head of the tree. Which mean we need to reallocate the nodes. WHich is really just the immediate children, since its all sorted already.
According to the contraint of the problem, it doesnt matter which child node takes the pace of the removed node. Just has to stay sorted as a bst.

So step 1. FIND THE NODE.
And now that I think about it, we also want to be abe to reference the parent. We should pass that down in a dfs so we know what node to point to next.

