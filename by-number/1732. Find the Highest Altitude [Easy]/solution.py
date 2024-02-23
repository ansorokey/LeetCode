def foo(gain):
    # we start at a gan/loss of 0
    maxAlt = prevAlt = 0

    # iterate through every gain
    for g in gain:

        # our current height is the previous height plus/minus our change in gain
        curAlt = prevAlt + g
        
        # if our current height is greater, save
        if curAlt > maxAlt:
            maxAlt = curAlt

        # our current height will be used to figure out the next height
        prevAlt = curAlt

    return maxAlt

print(foo([-5,1,5,0,-7])) # expect 1
print(foo([-4,-3,-2,-1,4,3,2])) # expect 0


# Submission:
# Time: 31ms - 94.50%
# Space: 16.6mb - 63.70%
# Runtime: O(n)