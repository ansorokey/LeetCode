What is being asked here?

We are given an array where each point represents how high or low a biker has moved, from where they were last. Each point does NOT represent their current height, but the difference in height.
in the example [-5, 1, 5]
the -5 means they started with no gain or loss, and went down by 5.
0 + -5 = -5.
Then, from that point, they increased by 1.
Meaning -5 + 1 = x, or -4
And from -4, they went up by 5 again
So now -4 + 5, which is an altitude of 1.
So our current heights are 0, -4, and 1
In this case, 1 is the highest altitude. That is what we want to return.

So how do we approach this?
We want the highest altitude, so let's keep track of a maxAlt.
Wherever the biker start, they begin with 0 loss and 0 height gain, so our starting altitude will always be 0.
From there, we need to traferse through the array and compare if the prev alt + the current alt is greater than the max alt.
If it is, we assign it, 
Then we can assign the prev alt to be the current alt, an move on to the next.

Let's try it.