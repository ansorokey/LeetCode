def mergeAlternately(word1: str, word2: str) -> str:
    # a pointer for each word, and the array pointer
    i = j = k = 0

    # a result array of the length of combined inputs
    # this will prevent dynamic resizing
    # more efficient than using a string because each append
    # would require us to recreate that string, n characters n times
    res = [None for x in range(len(word1) + len(word2))]

    # using or instead of and to save us having 
    # to do a cleanup at the end
    while(i < len(word1) or j < len(word2)):
        # each character goes in the place of k,
        # inc k after each append
        if i < len(word1):
            res[k] = word1[i]
            i += 1
            k += 1
        
        if j < len(word2):
            res[k] = word2[j]
            j += 1
            k += 1

    # join res at the end, print it
    res = "".join(res)
    print(res)

mergeAlternately('cat', 'dog') # 'cdaotg

# Submitted:
# time: 41ms - 40.11%
# space: 17.4mb - 18.10%