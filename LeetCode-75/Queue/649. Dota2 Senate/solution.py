def foo(senate):
    # Make it easier to reference each party at the end
    partyMap = {
        'R': 'Radiant',
        'D': 'Dire'
    }

    # keep track of how many future senators a party can ban
    partyCount = {
        'D': 0,
        'R': 0
    }

    # reference the opposite party
    opposite = {
        'D':'R',
        'R':'D'
    }

    # Keep track of who gets to vote next
    queue = []

    # seperate variable to iterate through
    bans = senate

    # repeat this so long as there are opposite members in the party
    banned = True
    while banned == True:
        # start by assuming we didn't perform any bans
        banned = False

        # iterate through remaining votes
        i = 0
        while i < len(bans):
            senator = bans[i]
            otherSenator = opposite[senator]
            
            # if the other party cannot ban the current memebr,
            # we add them in line and give them a future ban
            if partyCount[otherSenator] == 0:
                partyCount[senator] += 1
                queue.append(senator)
            else:
                # if the other party has a ban,
                # assume they used it on this person
                partyCount[otherSenator] -= 1
                banned = True

            i += 1
        
        # now we iterate again in the same order of valid votes
        bans = ''.join(queue)
        queue = []

    return partyMap[bans[0]]




print(foo('RD')) # expect Radiant
print(foo('DR')) # expect Dire
print(foo('RRR')) # expect Radiant
print(foo('DDD')) # expect dire
# print(foo('RDRDRDDDD'))
print(foo('DDRRR')) # Expect Dire

# Submission:
# Time: 62ms - 47.28%
# Space: 16.7mb - 95.30%
# Runtime: O(n)?