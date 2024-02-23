What is being asked here?

Given two trees, find out if their leaves (end nodes) from LEFT to RIGHT share the same sequence.

This means we have to depth first traverse each tree, and keep track of their leaf nodes. After doing that to both trees, compare the results.

Since we're keeping track of noes this time, we need to store them. A list works fine. Recursion would be easier, but let's try this iteratively.