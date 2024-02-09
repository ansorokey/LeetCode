def foo(s):
    # use an array to join all acharacters at once
    # more efficient than rebuiling the string with each addition
    output = []

    # iterate through the given string
    for c in s:
        # if it isn't a star, we add it
        if c != '*':
            output.append(c)
        else:
            # otherwise, it is a star, which we ont need to add
            # and we need to remove the last (leftmost) character
            output.pop()
    
    # join the string and return
    return ''.join(output)

print(foo('abc*')) # expect 'ab'
print(foo(s = "leet**cod*e")) # expect lecoe
print(foo(s = "erase*****")) # expect ''
 

# Submission:
# Time: 132ms - 77.95%
# Space: 18.3mb - 60.19%
# Runtime: O(n)