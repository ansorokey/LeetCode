What is being asked here?

Given a string, we want to create a new string in which the order of the WORDS is reversed, and each word in the new string is separated by a single space.
A WORD will by any alphanumeric characters that doesnt have a space in it.

"hello world" should become "world hello"
and "1 2 3 4" should become "4 3 2 1"

So in order to do this, we should:
A. Get all the word into an array and
B. Reverse that array into a string

If the array is already reversed, then all we'd have to do is join at the end.
So the easiest solution would be to make an array, iterate through the back of the string, and append words.

Finding a word would require us to start from the back of the string. We'd need to create a slice from the start of the word to the end.
e will always start with an index of length - 1, and decrememnt until we find a non-space character.
Start should have the same index as end.
We should decrement it until we find a space OR util we are out of bounds. That will be the slice we append to the array.
After we finish that slice, we want to make the end index the same as start, which sould be a space or out of bounds.