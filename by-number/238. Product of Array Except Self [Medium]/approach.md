So what is being asked here?

We are given an array of integers
[1, 2, 3, 4]

We want to return an integer array where every index represents the entire array multiplied together, excluding that number
So that would look like
[2*3*4, 1*3*4, 1*2*4, 1*2*3]
and the end result would be
[24, 12, 8, 6]

Any mathematical pattern is purely coincidental. This was for demonstrative purposes only.

In addition, we are given a contraint of making this run in O(n) time.

So to start off, I think I want to brute force this, break the constraints, and solve this in O(n^2) time. That's the easiest and most straight forward solution.
To do that, I'd create a result array.
Then I'd start looping through the array.
We'd need to create a running oroduct, which we can set at 1.
In the second loop, we'd run start to finish and check to see if the second index equals the outer index. If so, we don't multiply the running product with the current index.
After completing the inner loop, append the product and start over.
Return the resut array.

Brute force works. Now what can we do to reduce this down to O(n)?
An O(n) runtime means we need to avoid nested loops, but we can have as many parallel loops as needed.
So let's start with one.
We an probably keep a result array.
We can probably keep a running product.

I'm stuck and lost, so let's ponder the result a bit.
Looking at the desired end result, I noticed that the last index should be the product of everything before. So let's aim for that small goal first.
In order to get the product of 1, 2, and 3 in that position, we'd have to multiply the number that came BEFORE and set that as the current index value.

Okay, we did that. 
Now what if we made an array doing the same thing, but going the other way?
Same process.
Loop.
Check if theres a value before(after in this case).
Multiply running
set it as current.
Let's see what we get in a second array.

Oh my goodness i think we've got it.
We now have two seperate arrays of where the first and final values are what they need to be, and 1. Which multiplied results in itself.
So if we iterate and multiply the values together, we should get a final result!

IT WORKS :O

Now for an added callenge, can we reduce the number of extra arrays and variables we use?
Instead of two result arrays, can we use one by multiplying the backwards array in place?
THIS ALSO WORKS and only created two extra variabes! A constant running and an output array of size n.