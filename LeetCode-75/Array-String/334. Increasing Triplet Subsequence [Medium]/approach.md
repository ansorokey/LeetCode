What is being asked here?

We are given an array of integer nums of at least length 1.
Our task is to see if there are any three spots in the array where the index and the value at the index all increase.
Meaning if we start at any index, `i`, will there be an index further down that also has a larger value at that index.
For example:

[1, 0, 2, 0, 3]
The indexes
0 -> 2 -> 4
work because the values
1 -> 2 -> 3
also increase as they go.

We do not need to return the indexes or values, we only need to return a boolean result if a triplet like that is found.

So how do we approach this?
Let's start with brute force.

We could start by iterating through the list.
The first index would have to be the smallest since we dont know what else is in the list.
From that index+1, we could iterate again until we find any value larger than the first given value. hat would be the second index.
We could then repeat that one more time and see if we find a value bigger than the second.
If we find a match at the end of that, then we can return true

If we exit all the loops without returning true in the last inner loop, then we've found nothing and we can return false.
So maybe a while loop with three parallel inner loops.
while i is less tan the legth of nums,
    find the first,
    find the second,
    find the third

return false

Let's try that.
this works until we use an edge case where there is a huge spike in the middle, like
[1, 100, 2, 3] 
We need some way of bypassing huge spikes, or some way of going back to the second value.
If we nest the third loop into the second, that'll go back to the first larger value