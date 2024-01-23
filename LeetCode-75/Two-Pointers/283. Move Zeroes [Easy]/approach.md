What do we need to do?

We need to find a way to move all 0's so that non-zero elements are up front, and 0 elements are to the back.
The challenge is to do this in place, the goal is to do it in as litle operations as posible.

Do not return anything, just modify the array input.

So if we were to brute force this the easiest way possible, we could just bubble sort. But we could be given an absoutely massive input length, and we'd definitely hit runtime.
We could also use a faster sort operation to reduce bubble's O(n^2) down to O(n log n).

Is there any other way we could do this in a single iteration?
Let's think.
We could start by iterating from the first element.
We could continue until we find the index of a zero.
Track that.
Continue util we find the index of a non-zero
once we have a zero and a non zero, swap them in place.

So maybe we need a poniner that sits at the first index of a zero, or rather the last index swapped. 

One pointer should incrememnt until it finds a zero.
Another pointer should incrememnt until it inds a non zero.
When both are in place, 
swap the array values.
Then the zero pointer needs to find the next zero,
and the non poiter neeeds to find the next non-zero
if the nn-zero pointer ever leaves bounds, we're done