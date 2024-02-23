What is being asked here?

We are given two integer arrays.
Our goal is to return an array contaiing the number of unique integers that do NOT show up in the other array.
if we had [1, 1, 1] and [2, 2, 2] then our answer would be 1, 1 since 1 is not in 2, and 2 is not in 1.

Since we need to eep track of unique instances, we can create two sets. One for each array. The quantity of each doesnt matter. That can be done with two for loops.

After we create the sets, we can reate two variables to count the unique istances in each set. hen we can iterate through each set, and incrememnt as needed by testing if a certain key is on the other.

return the array with the two counts.

I DID NOT READ WELL ENOUGH. We are returning a LIST of all the unique numbers, not a count. Same things apply, basically.

It works! But can we reduce the number of loop and objects we used?
