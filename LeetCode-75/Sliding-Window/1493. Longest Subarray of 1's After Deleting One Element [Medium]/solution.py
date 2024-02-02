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
        # meaning at least two 0's have ben reached
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
# Time:
# Space:
# Runtime: