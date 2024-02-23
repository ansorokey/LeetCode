def reverseWords(s: str) -> str:
    end = len(s) - 1
    words = []

    while end >= 0:
        # find the first valid character
        while s[end] == ' ':
            end -= 1
            # if we break bounds, there are 
            # no more words to find
            # return early
            if end < 0:
                return " ".join(words)

        # start the search for a space at the
        # index of end
        start = end

        # find the first space
        while s[start] != " ":
            start -= 1
            # if we're outside the boundry,
            # and end is valid,
            # then the entire slice is a word
            # exit
            if start == -1:
                break

        # start and end are one ahead the indexes we need to slice
        # append that words to output
        words.append(s[start+1:end+1])
        
        # advance loop ahead to start, which is a space
        end = start

    return " ".join(words)

print(reverseWords("1 2 3"))
print(reverseWords("x"))
print(reverseWords(" x "))

# Submission:
# Time: 47ms - 22.49%
# Space: 17.4mb - 42.88%
# Runtime: O(n)