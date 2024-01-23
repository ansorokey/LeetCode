What's being asked here?

We are given two strings. We want to find out if one string can be created by deleting none or more characters.
More specifically, we want to find out if the substring can be made by walkin through the main string.

So in order to do that, maybe we could do something as simple iterate through the main string.
At every spot, we could check to see if the current character matches the first spot in the substring.
If it does, we can move to the next character in the substring and see if that matches further down.
By the end of this loop, a match will have the pointer extend outside the substring, or equal its length

return a boolean.