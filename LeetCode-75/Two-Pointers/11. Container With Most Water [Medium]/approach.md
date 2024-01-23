What is going on in this problem?

We are given an array of integers.
Each of these integers bascally represents the height of a wall of  container.
The length of the array itself represents the bottom of the container.

The goal is to find out what two height at what distances create a container with the most volume.

if we have an array 
[9, 3, 3, 3, 8]
Then the most water we could hold
would be two walls of height 8 (because we need to use the shorter of the two walls, otherwise water would spill out) at a ditance of 4 (index 4 - index 0) for a total volume of 32 units.
So our equation is Min(h1, h2) * (i2 - i1)

How do we start this?
Well if we have two walls, we proably want two pointers. One at each end. This will also start us with the maximum length, since changing walls will only decrease the length and total volume.

lets say we have an array 
[1 2 9 3 3 3 9 2 1] l = 9
starting from the first walls and going in, the volumes are:
1 * 9, 2 * 6, 9 * 4
which is
9, 18, 36
Clearly, this show that moving inwards can result in a better volume.
The question is, ho do we decide when we want to move inwards?
from step 1 to step 2, we can see that the next index is larger for both pointers. They're also larger than the opposite pointers. So whch matters more, the opposite pointer or the current pointer?
Lets make up another example

[2, 0, 0, 0, 2, 1] l = 6
from the outer edges, the volume is 
1 * 6 = 6, and if we move in by 1, the volume becomes
2 * 5 = 10
now the same exampe where the first is just one smaller
[1, 0, 0, 0, 2, 1]
In this example, the wall height would never increase because it's neighbor doesnt increase.
So let's assume it is only worth it to move inwards if the current pointer is less than the opposite.

AS for the volume, we should probably kee trac of the maximum v encountered, since that's what we want to return, not the current volume we could make at the indexes.

After doing some basic code, I'm stuck. Now that I've laid it out, I see that I have no way of further decrementing the pointers if they land at an equal height and the neightbors are less than the current height.

Maybe instead of moving both pointers at the same time, I should pick one instead?
