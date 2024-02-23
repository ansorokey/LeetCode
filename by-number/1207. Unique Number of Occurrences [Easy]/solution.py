def foo(arr):
    # keep track of element counts with a hashMap
    intCount = {}

    # iterate through list
    for n in arr:
        # if we've seen this integer
        if n in intCount:
            # incrememnt it
            intCount[n] += 1
        # otherwise we havent seen it
        else:
            # add it to the count
            intCount[n] = 1

    # Now we have a hashmap of integers and their counts
    # create a set to track just the counts
    uniqueCounts = set()
 
    # iterate through the counts
    for c in intCount:
        # if this number is already in the count
        if intCount[c] in uniqueCounts: 
            return False
        # otherwise, 
            # add it
        uniqueCounts.add(intCount[c])

    # we never found two matches, 
    return True

print(foo(arr = [1,2,2,1,1,3])) # true
print(foo(arr = [1,2])) # false
print(foo([-3,0,1,-3,1,1,1,-3,10,0])) # true

# Submission:
# Time: 40ms - 64.09%
# Space: 16.6mb - 95.40%
# Runtime: O(n)