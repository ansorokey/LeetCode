What is being asked here?

We are given an array where the index represents a child and the value represents how many candies they have.

We have x number of extra candy.
The goal is to return an array of boolean values, where each boolean is whether or not giving the child of that index all the extra candy will leave them with the most candy of the group.

So off the bat, we know we need to return a boolean array.
The array will be the same length as the input, since each index is a child.
We need to find out if a child's candy plus extra candy results in the most candy. So we need to find the max value among the children, and use that as our comparison point. The boolean value can be true if it is greater than or equal to that value.

Finding the max can be one iteration, and then populating ht resut array can be another.