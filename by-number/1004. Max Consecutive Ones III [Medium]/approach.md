No seriously, what is actually being asked here.

We are given a binary array as one input. That means any element is either a 1 or a 0.
We are also given an integer k. K is the maximum number of 0s we can turn into 1s.
So if we had 1, 0, 1 and a k of 1, we could turn 1 0 into 1
Which would be 1 1 1

Our goal is to find the longest subarray length where each element is a consecuitive 1, with the possibility of flipping.

Okay, how would be start going about this? If we break the problem down, we have two tasks. One of which is finding the longest subarray of consecuitive 1s. The other sub-task is turning a 0 into a 1.
So the first focus should be on fiding the longest subarray of 1s as is. Let's code that out.

Since our output will be the length of the longest subarray, we need to keep track of the lonhest length.
But each length could be different as we traverse the array, so we'll also need to track a second variable for the current lenth, and compare it to the max.

Since the subarray length can be variable, we could do one of two things to track length.
A. We use one pointer and start counting when we come across our first 0, and incrememnt with eac 0 after that.
B. We use two pointers to crawl through the array to denote the start and end of the subarray.

I think the first one pointer approach will be easiest to implement at this current stage. Let's start with this an code it out.

Mkay, that works for that specific portion of the problem. Now we want to find some way to incorporate the flipping.
How would we do that? Well, we're given a set number of zeros we can flip. So when we coe across a 0, we can flip it, an decrease the number of remaining flips available. From there, we can continue counting length as usual. 

What hapens when we come across another 0 and we're all out of flips? When we encounter this scenario, we would probably want to unflip the easrliest 0, and flip this 0 instead. But doing that is goin to change the count moving forward in a way that couldn't be easily tracked by a single counting variable.
SO now we probably want to move to a two pointer window approach.
We can still keep the counting variable, but with a second pointer, we can keep track of the last 0 position. That way, when we flip it, we can move on to the next in line.

Let's first refactor our one pointer aroach into a two pointer approach.

OH BOY I am sruck. WIn the case of 0 flips given, I need the program to know when to move that starter pointer forwards.
Let's take a step back and look at this problem again.
The goal is to find the LONGEST length of consecuitive ones, where k number of 0's can be counted as a 1.
Since that can be any length, we need a window that can adjust to that size.
That means there s a left and right boundry for this window (start and end)
To iterate through the array, one of these points has to constantly be moving forward.
The other needs to be catching up on certain conditions.
So we can have end incrementing, and start catching up.
When end incrememnts, it can only land on a 1 or a 0.
Nothing significant happens when end lands on a 1. 
When end lands on a 0, two things can happen.
    Either we can flip it and count it as a 1, and proceed as normal
    OR
    we need to catch the start up to the next working position

What does it mean to catch up the start? The starting pointer can only be on one of two things.
Its either on a 1, in which case nothing really needs to happen.
OR it's on a 0.
If the start is on a zero:
    it is either already flipped, 
    OR needs to advance forward to return that flip.
    Advancing forward means PASSING a 0, so the number behind it should be 0.

Now what if we mix some of these conditions?
What if start is on a 0 and end is on a 1, and we have no flips AT ALL?
Then start needs to advance until it reaches a 1.
And the other way around?
start on 1 but end on 0?
If we know we cant do any flipping, then we need to advance start to the next available position past a 0,

So the most important thing to note is that when advancing start, it MUST pass a 0.

Now, let's try this again from scratch.