What is being asked here?

We are given a 2d integer array of length n that represents a SQUARE grid-matrix. N rows of n columns.
Our goal is to return the number of columns that would create the same array as a row within the matrix.

Seems simple enough, but let's not get ahead of ourself.
First of all, we need an integer output put, so we can start a counter at 0.
Secondly, we need a way to find out what every FULL column and every FULL row would make as an array, and keep track of that.
That means we should probably use a hashmap/set to store the array results.
Since we can't store an array as a value, instead, we could store them as strings.
While we're on that topic, do we need to store a value with that array as string key? Let's think.
We have a counter.
We iterate and create a set of rows.
We iterate and create a set of columns.
What if the matrix we were given was all 1's?
1 1 1 1
1 1 1 1
1 1 1 1
2 1 2 1
The first time we add '111' to the set, it's just added
But we have a second and a third copy of the same row. So we probably want to use a hashmap to also track the number of duplicate row results.
hat would give us a hashmap of '111': 3

Did the problem ask for the number of UNIQUE pairs? Nope! Any row-column pair is a pair! Taking a quick look at the math involved, I think the number of pairs for duplicate row would just be count += value * value

Going back to the actual process, after we get a map of both, we want to iterate through one map's keys.for every key, we ask if it exists on the other map.
If so, the count += the value * value.

Now all we need to do is know how to iterate through the matrix.
Getting the rows is easiet, it's just every sub array.
Getting the ows just requires us to flip out indexes.
There might be a more efficient way that I can't think of right now, but creating one extra list, adding the ints as strings, an joining them at the end seems easiest.

I think we have a grasp on the problem? Let's try it.