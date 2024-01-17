"""
In this approach, we use two pointers to modify the split list
in place, without creating a second helper array
"""

def reverseVowels(s: str) -> str:
    # create an array of the split characers
    sp = [c for c in s]

    # create a set of all vowels
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
   
    # pointers to the left and right ends of list
    l = 0
    r = len(sp) - 1

    # continue to swap out vowels until the pointers cross
    while l < r:
        # find the next left vowel
        while sp[l] not in vowels:
            l += 1
            # wont stop until we find a vowel, 
            # so we can break out if we exceed bounds
            if l >= len(sp):
                break

        # find the next r vowel
        while sp[r] not in vowels:
            r -= 1
            # wont stop until we find a vowel, 
            # so we can break out if we exceed bounds
            if r < 0:
                break

        # prevent us from re-swapping already swapped vowels
        if l > r:
            break

        # swap
        temp = sp[l]
        sp[l] = sp[r]
        sp[r] = temp

        # push the left and right pointers by 1
        # otherwise, they're at a vowel and will never move to the next
        l += 1
        r -=1

    return "".join(sp)

print(reverseVowels('hello'))
print(reverseVowels('bbbbbbb'))
print(reverseVowels('lEetCoDE'))

# Submission:
# Time: 42ms - 95.44%
# Space: 18.8mb - 19.14%
# Runtime: O(n)