def foo(nums):
    # pointers and result start at 0
    start = end = maxLength = 0
    # we can delete one digit
    deleted = 1

    # iterate through array
    while end < len(nums):

        # geedy: subtract a digit at every 0
        if nums[end] == 0:
            deleted -= 1

        # this will only activate if the above happened, 
        # meaning at least two 0's have been reached
        while deleted < 0:
            # move the start past the first 0
            start += 1
            if nums[start - 1] == 0:
                deleted += 1

        # compare lengths
        curLength = end - start
        if curLength > maxLength:
            maxLength = curLength
        
        # advance the end
        end += 1

    # return
    return maxLength

print(foo([1, 1, 1])) # expect 2
print(foo([0, 1, 1])) # expect 2
print(foo([1, 0, 1])) # expect 2

# Submission:
# Time: 465ms - 68.49%
# Space: 20.2mb - 55.82%
# Runtime: O(n) now that I think about it? Actually, no.
# iterating throuh the list is On. If every elememnt was a 0, we'd be
# advancing start by 1 every step.
# AT MOST that could onl ever be 2n, which is still On reduced