JEEEZ this problem is asking a lot. But...what exactly is it asking?

It gives us two strings.
It wants us to find out if these strings can turn into one another.
The only way we're allowed to modify the strings are:
    1. Swapping the position of any TWO characters that exist in the string.
    NOT adding new charcters or turning the characters into brand new letters.
    For example, 
    aaxxbb => abxxab
    Here, we were allowed to swap the places of ONE a and ONE b

    2. Turning all instances of one character into another. Again, the characters they can turn into MUST be in the string already. Anything that gets transformed MUST have its opposite also transformed into itself.
    For example,
    aaxxbb => aabbxx
    here, we switched all x into b, and all b into x

The steps above can be combined as many times as needed.
So how do we even start going about this?

Let's start with what we can see.
Obviously, two strings cannot turn into one another if they aren't the same length.
And, they can't turn into each other if they don't share the exact same characters. So that's an easy case for returning fale earlier.

That also means that two valid strings at least share the following:
    They are the same length.
    They have the exat same characters.

For now, let's start our function off here.
How do we track the characters a string has?
We can iterate through both, and create a set for each string. If either has a caracter the other doesn't, its invalid.

So at this point, we've removed any strings that aren't the same length, and we've removed any strings that are the same length, but have different characters.

Now, based on the rules above, we need to figure out if they can become each other.
Rule 1 states that we can swap any two characters.
AND we can do this any number of times.
That basically means we can sort the entire string if we wanted to.
'abbccc' would be valid as 'cccbba'
So odrer has no bearing on this whatsoever.

If order has no meaning, then we can focus on rule 2.
Rule 2 says that we can turn one character into another and vice versa.
so 'abbccc' could become 'caabbb'

So if we'e made it to this point, then what is the common trait between these two strings?
They have the same length!
They have the same characters!
AAAAAAAAND
They have the same INSTANCE COUNT!!!
if we look at abbccc, there are 1 a, 2 b and 3 c. in caabbb there is 1 c 2 a 3 b
1, 2, 3 and 1, 2, 3
So they key to this is tracking the instance counts of these strings, and seeing if they match! We're already tracking them with a hashMap, so we can just count the instances and compare them to each other again.
But before we do that, how would we handle multiple similar counts? if we had 'aabbcc', it would be 2, 2, and 2
Oh, well I guess we could just count them again.
2: 3
3 instances of 2
OKAY let's try it

IT WORKS! Not the greatest runtime, but it WORKS!