def reverseVowels(s: str) -> str:
    # create an array of the split characers
    sp = [c for c in s]

    # create a set of all vowels
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
   
    # filter out the vowels of the string into a list
    vArr = [c for c in s if c in vowels]

    # create a pointer sarting from the back of the vowels list
    v = len(vArr) - 1
   
#    iterate through every character of the split list
    for i in range(len(sp)):
        # if we come across a vowel
        if sp[i] in vowels:
            # put the last vowel of the vowel list in its place
            sp[i] = vArr[v]
            # move the vowel pointer down by one
            v -= 1

    return "".join(sp)

print(reverseVowels('hello'))
print(reverseVowels('bbbbbbb'))
print(reverseVowels('lEetCoDE'))

# Submission:
# Time: 52ms - 72.00%
# Space: 19mb - 16.71%
# Runtime: O(n)