What is being asked here?

We are given an array of positive and negative integers.
The absolute value is how big the asteroid is.
Positive means it is traveling RIGHT, negative means traveling LEFT
When two asteroids collide, the larger (bigger absolute value) survives and the smaller (absolute value) diappears. Both disappear if they were equal.

Our goal is to return an array that represents all suriving asteroids after any collisions that would have happened.

How do we approach this? Before we figure out collisions, we need to make sure we know how to get an absolute value. I'm sure there's a built in math function for it, but let's understand the logic first.
The abolute value of a number is a positive value. So to make any negative number positive, we can just multiply it by -1.

Next, we need to iterate through the given asteroid array.
Two asteroids going in the same direction will never hit.
Left left, right right.
So they can just be added to the result.
In addition, two asteroids traveling AWAY from eachother in opposite directions will also never hit
left right
So the only time we need to check a collision is when the two asteroids are traveling
right left
And at that point, we check to see who survives.
IF there is a survivor, we add that one.
Otherwise, we add nothing.

Now what if we had one HUGE asteroid going right, and nothing but small asteroids going left?
Well, first we'd have to add the first asteroid.
Next, we get to the second asteroid.
We can see they ARE colliding, so this current asteroid does not get added.
The result stays the same.

How about the other way?
All small asteroids first going right and then one huge going left?
Well, we'd have an array full of small ones.
Then we get to the big one.
We can see a collision.
The large one survives and gets added to the end of the array.
But we know that it needs to collide again, so we can't just stop after adding it.
Instead, before we finish adding it, we remove the one it crushed.
Now the one before it is the last asteroid.
Collide again.
Remove the last, change the last, collide again.
Now, it looks lie we keep repeating this process over and over again until we stop colliding. That sounds like a while loop with a collsiion ondition.

Lastly, what if our current and last both crash?
Then neither gets added, and we grab the last again.

So at every step in the iteration, we will do one of the following:
    add the last back to the end
    add the current to the end
    add the last AND the current
    remove the last

Let's start coding this out and see what it looks like.