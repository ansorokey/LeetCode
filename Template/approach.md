What is being asked here?
Given two strings, we want to find the smallst substring that DIVIDES both str1 and str2

If we were to look for just the smallest substring, 'c' would be the answer for inputs of 'cat' and 'cook', but this does not divide them. 

In order to properly divide the strngs, the smallest common substring has to be repeatable such that it could compose the entire string.

That is why 'ab' would be the output for 'abab' and 'ababab'

So how do we find that? Well, inorder to be evenly divisible between the two, a substring would have to start the same way, so we can at least begin with the first characters of each. Or, better yet, maybe we could begin wih the smaller of the two strings and work backwards. If the smaller string is not equal to the substring version of the larger string, retun an emrt result.

When would we want to stop? If at any point, 