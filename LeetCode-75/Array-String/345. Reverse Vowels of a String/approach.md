What is being asked here?

We are given a string of ascii characters.
We want to reverse the vowels within the string.
Reverse, meaning if we took all the vowels out of the string and started putting it back together again, we'd insert the vowels taken out last, first.

What are some ways we could approach this?
I think the first, less elegant solution would be to iterate through the string and create an array of all the vowels. We could also create an array of all the letters in the string on its own.
So something like

hello
[h, e, l, l, o]
[e, o]

Then, we could iterate through the fully split array, and every time we encounter a vowel, we replace it with one from the vowel array, starting from the back.
So we would need a seperate counter for the vowels to go backwards from.
At the end, we combine all the characters in the full split array and return it