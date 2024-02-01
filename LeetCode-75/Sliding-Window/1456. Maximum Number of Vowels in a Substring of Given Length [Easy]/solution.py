def foo(s, k):
    # result and comparison counts
    maxcount = 0
    curcount = 0

    # points for start and end of substring
    start = 0
    end = 0

    # constant lookup for vowels
    vowels = {'a', 'e', 'i', 'o', 'u'}

    # if end is ever greater than the length, 
    # then the substring is less than k length
    while end < len(s):
        # is the next character a vowel?
        if s[end] in vowels:
            # inc the count
            curcount += 1

        # we only need to start comparing vowel counts when the
        # substring is of proper length
        if end - start == k-1:
            # check the max count
            if curcount > maxcount:
                maxcount = curcount
            
            # the start needs to move forward, which means
            # a character needs to be left behind
            # if it was a vowel, decrease the current count
            if s[start] in vowels:
                curcount -= 1

            # advance the start pointer
            start += 1

        # advance the end pointer
        end += 1

    return maxcount

print(foo("abciiidef", k = 3)) # 3

# Submission:
# Time: 111ms - 83.15%
# Space: 17.4mb - 67.29%
# Runtime: O(n)