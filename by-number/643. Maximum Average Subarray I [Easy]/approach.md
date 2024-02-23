What is being asked of us?

We are given two inputs.
An array of nums,
and a length of k

Our goal is to find the maximum average within the given array with a contiguous length of k

so for 
[1, 2, 3, 4, 5], k = 2,
the contiguous sub arrays would bwe 12, 23, 34, 45,

How can we approach this?
Well first we' need to iterate through the array. Since we are only checking the subarray lengths of k, we can stop at the index of length minus k MINUS 1
Anything past that would be too shot of a subarray.

The simplest method is to simply use nested loops, but this exceeds the time limit.

How can we reduce this into a single iteration?
Well, in order to mantain the wndow, we need a start and a finish. So let's keep track of two pointers.
We can continue to iterate while the end is less than the length of the nums
Now , we need to move the end into position. So until the end is in its place, we just incrememnt it.
We only ever move the starting pointer when our window is at the right length
We alo only ever check for an average if it's at the right length too.

In addition, at every step of the windo wmoving, we need to add the next number, and subtract the last