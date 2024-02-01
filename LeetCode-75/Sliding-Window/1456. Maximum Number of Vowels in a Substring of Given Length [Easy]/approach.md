What is being asked here?

We are given a string, and a length. Our goal is to return the MOST vowels in a single substring of length k.
We don't need t return the substring with the most vowels, only how many vowels it does contain.

What's our approach?
Since we want to return a number, let's keep track of our result starting at 0.

Next, we want to iterate through the string.
Since we're using a substring, it will have a start and an end. We can use pointers to keep track of the start and end.
With every step, we want to check if the next and last characters are vowels.
When we leave a vowel, the count should decrease by one.
When we add a vowel, we should increase by one.
That means we should also keep track of a seperate current count variable to compare to the max, and overwrite when larger.

Let's start.