What is being asked here?

We are given an array of integers and a sum.
In a single 'turn', our goal is to remove a pair of elements in the array that add up to the given sum.
The value we want to return is how many times we can remove TWO numbers from the array that sum to k.

How would we go about brute forcing this?
The easiest way would be to nest loops and modify the input array, removing the values that sum to k each time.
We can stop when there are no more values that sum, whch we can keep track of with a boolean that says if we subtracted or not.
As for keeping track of values that can add together we can keep a hashmap of values and indexes we've passed.

Let's just start with that.

Actually, now that I'm coming back to this, why even modify?
We can do nested loops, but advace the beginning position of the enxt starting index so we don't ever use that num again.

Okay, that worked for the first example, but failed when we came across two other complimentary numbers
in k = 6, [3, 1, 3, 2, 3],
index 0 works with BOTH index 2 and index 4
We only want complimentary numbers to count once
so what if we bump the current index as soon as we encounter a pair?
Or in this case, break the inner loop

That acually still doesn't work, because it only removes a sigle digit from the equation. The num it paired with is still available.
Both the current and partner numbers need to not be counted anymore.

So let's go back to the first approach.
Iterate through once, and see if we've passed a partner.