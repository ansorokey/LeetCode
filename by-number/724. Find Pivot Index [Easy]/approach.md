What is being asked here?

We are given an array of integers.
The goal is to find the INDEX of the number where everything to the left adds up to everything to the right.
Specifically, the leftmost. Meaning if there are two indexs that share the same sums, return the first from left to right

So how do we approach this?
Well we need two piees of information here.
The sum of everything to the left of a number, and the sum of everything to the right of a number.
We can do that in two seperate steps.
Going forwards though the array, the sum of everything to the LEFT of the first element is 0, since there's nothing there.
Then at index 1, the sum is 0 (the last sum) + el1
Then it the last sum plu el2
etc etc
When we get to the last element, the sum should be everything from 0 to el - 1, and then the same going backwards.
Ideally, we might even be able to do this using only two variables to store the left and right sums.
The first iteration forwards, we can get the entire left sum.
Them going backwards, we can begin building the right sum, and subtracting the digits to the left every time we move.
BETTER YET, we can flip the order, since we want the LEFTMOST index, if there is a pivot point. If we get through everything and havent retrned the index, jut return -1.

let's try!

It worked and submitted well! But looking at this, id I really need to do anything fancy for the right sum?  could have just gotten the sum of the array in one go.