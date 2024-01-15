The final result we want to achieve is a single string composed of the characters in the given strings, starting with the first.

That means we add to the string char1 from string1.
After that, we add char1 from string2.
Then char2 from string1, and char2 from string2.

Each string is guaranteed to have a length of at least 1, and only made up of english characters.

Since one string can be longer than the other, if we can add whatever is left of the remaining string to the end of the result.

So to begin tackling this, we would want to iterate through both strings at the same time.
To reference which character needs to be added, we can use index pointers, and incrememnt them as needed.

To be slightly more efficient on space, we can make the result an array of length s1 + s2, and join it at the end.
Using this, we would want to use an additional pointer to reference where to put it in the array
We could also just append, but this seems more accurate

Since we need to iterate through all characters of both word1 and word2, this should have a runtime of O(a+b)