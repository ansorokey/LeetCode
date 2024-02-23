What is being asked here?

Given an array of 1s and 0s, what is the longest length of consecuitive ones if we MUST delete a single digit.
so 1, 1, 1, would be 2, since we MUST delete a digit

How do we approach this?
This looks like a dymanic sliding window. So we should have two pointers for the start and end.
We shold also keep track of a max and current length.

We also NEED to delete a single digit. When possible, that digit should be a 0. And we can only delete one, so we can keep track of that with a boolean. 
If we get through the problem and never deleted a digit, we should just subtract 1 from the final result. Actually, maybe we should always subtract one from the final length anyway. if we have 1, 1, 1, the result would be 2. But if we had 1, 0, 1, the result would stll be 2, despite the actual length of digits being 3.

AS for finding the max length, we should incrememnt the end every step.
When we come across a 0, we should flip the boolean keeping track of deletions.
If we ever come across another 0, we would want to switch out the deleted digit, which would mean catching up the start pointer. In order to catch up, the deleted 0 would have to be outside the window, which means start would have to be one place ahead of that 0.

We can compare the lengths by subtracting the start index from the end.

Let's try!