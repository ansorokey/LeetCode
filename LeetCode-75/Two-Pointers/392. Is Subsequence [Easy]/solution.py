def foo(s, t):
    # set a pointer to the firs character of the substring
    p = 0

    # iterate through the main string
    for c in t:
        # if p is ever eual to or larger than the len
        # f the substring, we're already done
        if p >= len(s):
            break
            
        # if the current character matches the other character
        # move the other character up a spot
        if c == s[p]:
            p += 1

    # if the pointer matches the len of the substring,
    # we've found enough matches to verify the substring
    return p == len(s)

print(foo('ca', 'bcdea')) # true


# Submission:
# Time: 31ms - 91.59%
# Space: 16.6mb - 60.54%
# Runtime: O(n)