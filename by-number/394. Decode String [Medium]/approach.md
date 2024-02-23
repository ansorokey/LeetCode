What is this problem asking us to do?

We are given a string that is composed of NUMBERS (positive integers), SQUARE BRACKETS (always correctly paired) AND CHARACTERS (a-z)

Our goal is to return a string. Any numbers followd by characters within a square brackets should be repeated that many times.
We only ever need to repeat CHARCTERs. Number will not be include in the output, they are only for multipying their following string.

So what's our approach?
Based soley on the example, we need to trac a few different things.
1. The number of times a string has to be multiplied. Each time we come across a number, we need track it. But every tme we USE a number, we have to revert to the one that came before it.
So we should use a stack for this purpose.
2. The string. Since the entire input IS a string, and there can be several smaller strings contained inside, we need a way to keep track of what our current string is. Just like above, when we finish multiplying out a sring, we need some way to revert to the previous string. If there is no previous string, it should just be empty.
So we have two stacks at this point. One for the number, and one for the current string.
Next comes the main fuction of the problem, which is he concatenation of a string k times. We can make a helper function for that.

Lastly, the most important part is knowing when to call the helper funcion: ie when to concatenate a string. How do we know when we are done with the most inner portion of a string? Since a string is contained wthin brackets, then the ending bracket would be the time to take what we have built up and multiply.
After that, we can revert he string and number.
But let's look at examples to make sure.
2[a]3[b]
numstak would be 2, then we hit a.
Since the bracket ends the string here, we can pop the last number and take the last string and multiply.
If we revert both, then 2 the last num becomes nothing, and so does the last string. 

if the example was 2[a3[b]]
then the num stack would be 2, 3,
and the string stack would be [a, b]
pop each and we get 2 and a left on the stacks with the current string being bbb
So in addition, it looks like the last strig should be added on to the current string.

Let's start coding this out and see if we have the right idea.
 