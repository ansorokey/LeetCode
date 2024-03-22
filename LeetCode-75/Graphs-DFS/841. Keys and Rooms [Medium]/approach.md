What is being asked in the problem?

We are given a 0 indexed array of "rooms".
Within each room, there are integers that represent the "keys" to the other rooms.
The first room (room 0) is always unlocked. So we should always start there.
Then, we need to find out if we are able to visit/unlock every other room.
So the real question is less about visiting every room, but discovering if we are able to find a KEY to every other room 1 - n-1.

So we could probbly track this with a hashMap to bein with. Populate the hashmap with values 1 through n-1. This will represent all rooms. Let's call them haveKeys. Initially, we dont have the keys to any of these rooms, so we can set all those values to false.
Then we visit room 0.
There could be 1 key, there could be 3 keys, or there could be all the keys in this room.
So we need iterate through all keys in the current room.
And for every key in the room, we want to set that key value to true.

Every time we grab a key, we want to go straight to that room and collect they keys inside of that room. Since two rooms can have keys that lead back and forth to each other, we only need to visit that room if we dont already have that key.

After we've collected every key in a room, we want to move on to the next room ONLY if we have the key available to that room. Otherwise we skip over that room until we hit a room we can enter (have a key to).

When we get to the end of all the rooms, we need to check if we gathered every single key needed to oen all doors. In other words, our hashmap should be entirely true at the end.

So we need to do two things:
1. Iterate through all rooms
2. Iterate through all keys in that room.