What is being asked here?

We are given the head of a linked list.
Our goal is to assign an 0-index position to each node n the list, and then to re-order the list so all odd indices are first, followed by all even indicies, in their relative order.

This must be done in constant space and O(n) time.

So what is our approach?

First and foremost, we need some way to iterate through the linked list. We can do that with a pointer starting from the head.
As we iterate, we need some way of tracking if the current index is even or odd.
We could use a counter, but it ust occured to me that even or odd is a boolean result. So we could instead start with an isEven varable set to true, and invert it with each iteration, since index 0 is always going to be even.

Now that we can loop through the list and track even and odd indicies, we need some way to split them apart.
Since we are constrained to O(1) space, we cannot any arrays or hashMaps.
So instead, we need to overwrite pointers as we traverse.
Since we are still allowed to make varibles, we could create additional nodes.
One for odds, one for evens. Begin both off at None.
Now we have two heads we can use to later combine indicies. But we also need some pointer to add on to those lists.
LastEven and LastOdd can be used to keep track of whatever we need to add next.
At the end of this all, we want to have the lastOdd's next be the evensHead's next value, and have the last odd point to none
Fnally, return oddHeads's next which will be the first real node in the list.

Let's try it