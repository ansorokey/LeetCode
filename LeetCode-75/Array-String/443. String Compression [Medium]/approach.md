What is being asked here?

We are given an array of characters.
We want to return the input, modified.
For each unique, consecutive group of characters in the input, we want to add to the result that character and how many are consecutive.

For example, given 'aaabbc'
there are 3 a, 2 b, and 1 c,
which would be retrned as a 3 b 2 c 1

The begin, I think we would want to start be creating an output array. We can refactor later to modify the original input.

In order to count the length of a group of characters, we would need to iterate through the input.
While iterating, we want a counter variable to track the length.
We would also need to track when we hit a new character, so we'd also need a variable of the current consecutive character.
When w new character hits, that's when we want to add the previous character and length, and then reset both and continue.
We should also do that when we reach the bounds of the array.

Upon reading the problem better, we only need o append the length of the group if the length is greater than 1

Upon looking at example 3, I noticed that any value greater than 9 needs to be split as a string
12 chars would be etered as 1, 2

I think we have the basic example down, now we need to refactor so we only modify the input array.
How do we do that?
Well, we could have a pointer at where the next char would be added.
When we add a char, we overwrite the char in that position and inc the pointer.
If there's also a length, we add that and inc again.

I'm getting very lost, time to walk away and come back again later