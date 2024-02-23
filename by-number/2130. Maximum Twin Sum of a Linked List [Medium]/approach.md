What is being asked here?

God ol' leetcode, always finding the wordiest way to phrase something and give a junior dev an interview heart attack.
ALL THIS IS ASKING is to find the greatest sum of pairs in a symettrical linked list. By symetry, we mean that each node has a pair at the opposite, even index.
First and last, second and second to last, etc.

How do we approach this?
Well we know we'll be checing the sums of the values of nodes, so we can start off with a variable to track the current max.
Next, we need to know the length of the linked list so we know what indices to pair togeher, so we need a length variable and to iterate through using a pointer.
Once we have a length, we can figure out which nodes are pais and add their values.
Since we want to keep track of values and indicies, we could probably store all the values in an array. A map is uncecessary since we're just looking at one value at a 0 index.

Then we can iterate through thalf the array. And I think that'll do it? Seems to easy to be true, but let's try it.