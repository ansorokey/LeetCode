What is being asked here?

We are given two inputs.

n+1 (for some reason) is the number of cities. So it is also the exclusive end boundry.

connections is a series of roads where a leads to b.

currently, these roads all connect differently. Our goal is to form the road paterns, see what connects to what, and then find out how many changes would need to be made so that every city could eventually lead to city 0. In this case, all roads are ONE DIRECTION.

In order to do this, the first step I'd want to take is to create a map of cities.
for each city, i want them to have a set of all the cities they connect to.

After this is all completed, we iterate through every city from 0 - n.
Check each city they connect to until it hits 0 or until it hits an empty connection. If we hit an empty connection, then we increase the count of canges to be made, and we say this current number now leads to its parent number.
We should also be keeping track of all the cities that we have changed or know connects to 0 so we don't have to chec them anymore. A boolean array should do nicely.

So now we know that whatever recursive action we perform also needs a parent umber passed in.That also means that when we pop back up to the parent, we need to say it no longer leads to the child.