What is being asked here?

We are given the blueprint of a class and an class method.
The class method will be passed in a time in milliseconds. What it should return is the number of times this method has been called where the passed in time was between time - 3000 and time
For example, if 3000 milliseconds is passed in, how many times was this method called where the time passed in was 0 - 3000?

Since we want to keep track of the number of calls made, we need a collection, and I think a list should work find. We'll add that as a class propery.