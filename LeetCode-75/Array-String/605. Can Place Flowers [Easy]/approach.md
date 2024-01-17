What is being asked here?

We are given an rray that represents places a flower could be planted.
We are also given the number of flowers we want to plant.
Flowers cannot be planted directly beside one another.
So what we could do is iterate through the array given to us, and incrememnt a counter when we find a flowerbed without any neighbors.

The steps we'd need to take are:
Create a counter at 0
Loop through the array until we find a 0 ( an open flowerpot)
-If the previous neighbor is 0 OR outside the array, AND the next neighbor is 0 OR outside the array, incrememnt the counter
when the loop is done, return a conditional check to see if the counter matches the given flowers number

This satisfies initial conditions but breaks when we have a series of 4 open flowerbed. That would mean we have a set of three overlapping a set of three flowerbeds.
So now, we need to check to see how many unique locations a flower could be WITHOUT sharing a potential neighor.
A simple fix could possibly be incrememnting the loop index by 1?
That would push the index forward just enough so the immediate neighbor is not checked.

Initially that fix did not work in python, only because we cant directly incrememnt the iterator from the range uing somerhing like i +=1
Instead, I translated it into a while loop, and this fixed it and worked for submision.