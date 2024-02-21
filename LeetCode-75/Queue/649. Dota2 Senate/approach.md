WOAH TIME TO DO SOME EPIC GAMER HACKING
I do not like dota, and I do not like having to learn anything about dota
But I do like a high paying job, so I will unfortunately do this problem against my will and better judgement.

What id this problem asking?
We are given a string of two parties.
R or D. Every R or D in the given string represents a senator who can vote.
Each senator has two actions. Ban the next senator of the opposite party, or win the vote.
The vote can only be won when the opposite party can no longer votee, meaning they have all been banned.

So what is the approach here?
Well, there can be several rounds of voting.
There MUST be a winner.either R or D.
Consecuitive R' and consecitive DD's will never ban the next senate
So the important thing to take note of here is RD and RD in the given string.
Actually, since the last senator can vote off the first, we need some way to test that too.
Basically, it sounds like we'll be looping through an input and reducing it until only one party remains.
At any given point, we want to concern ourselves with the NEXT in line.
If the next in line is an opposite party, we ban it. 
If we're at the end, we need to the check the front.
So maybe we can keep an array constantly updated, and keep iterating through it until we've hit a length of 1.

OOOHHHHHHHH I competely misunderstood this. A senator can ban ANYONE'S vote from the other party. Not just the one directly next to them.
That's where the issue came in.
Okay, now that we have a better understanding of this, let's figure this out.
We still need to iterate through each senator's vote.
If we start on a D and there's an R later on, we want to remove the r's future voting ability. SO do we do it fom the back, or do we do it from the front?
One way we could do it is by iterating through the current valid votes and making a count of how many of that party we've encountered. If we encounter a member of the opposite party, then we can decrememnt that count and skip their turn. If we reach an opposite member, and there exists another member