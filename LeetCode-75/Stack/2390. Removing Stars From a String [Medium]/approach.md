What is being asked in this problem?

We are given a strng input.
We want to return a string output.
The string we want to return is the input MINUS all stars, and MINUS the first non start character to the left of the star.

How would we go about this?

First of all, we need an output. Since we'll be making a string, we can use an empty string, but an array wors just as well for more space, and lets us make the output all at once at the end. So we will have a result array that we join.

In order to add to the result array, we need to iterate through the given input.
We should add every character to the end of the result array as if we were building a string.
But when we come across a star, we should NOT add it. In addition, we should also remove the last character added to the end of the array.

After we are done iterating, return the joined array. 
Let's try it!