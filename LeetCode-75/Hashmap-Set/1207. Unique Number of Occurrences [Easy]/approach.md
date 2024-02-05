What is being asked here?

We are given an array of integers. The goal is to return if the NUMBER OF TIMES each integer appears in the array is unique, NOT if the integer itself is unique.
for example, [3, 2, 2, 1, 1, 1] would return true.
There is ONE 3, TWO 2, and THREE 1.
If it was [3, 2, 1] then there would be ONE 3, ONE 2, and ONE 1.
We're checking to see if the count of each integer is unique.

So how do we approach this?
Well, obviously, we need to iterat through the array and count each instance of the elements.
We can keep track of element count with a hashMap

After we have a count of each, we can iterate through the counts and check the values. I guess we could use a set to check if we've een that value. If we have, return false immediately. Otherwise, eep going. If we ge through the array, we aven't found two similar counts, so we can return true.

Let's try it.
