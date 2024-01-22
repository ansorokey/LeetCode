# def foo(chars):
#     # brute force output array
#     res = []

#     # track current num of chars
#     l = 0
#     cur = chars[0]

#     # iterate through chars
#     for i in range(len(chars)):

#         # if we find another of the same char
#         if chars[i] == cur:
#             # inc len
#             l += 1
#         # if we find a different char, or the next
#         # index is the end 
#         if chars[i] != cur or i+1 >= len(chars):
#         # add char and length
#             res.append(cur)

#             # l greater than 9 needs to be split
#             if l > 9:
#                 temp = str(l)
#                 res += [c for c in str(l)]
#             elif l > 1:
#                 res.append(str(l))

#             # reset variables
#             cur = chars[i]
#             l = 1

#     print(res)
#     return len(res)

# def foo(chars):
#     # track current num of chars
#     l = 0
#     cur = chars[0]
#     # last = chars[0]

#     # pointer where we need to overwrite
#     p = 0

#     # iterate through chars
#     for i in range(len(chars)):

#         # if we find another of the same char
#         if chars[i] == cur:
#             # inc len
#             l += 1
#         # if we find a different char, or the next
#         # index is the end 
#         if chars[i] != cur or i+1 >= len(chars):
#             # print(chars[i], cur, p)
#         # add char and length
#             # last = cur
#             chars[p] = cur
#             p += 1

#             # l greater than 9 needs to be split
#             if l > 9:
#                 temp = [*str(l)]
#                 for c in temp:
#                     chars[p] = c
#                     p += 1
#             elif l > 1:
#                 chars[p] = str(l)
#                 p += 1

#             # if i+1 == len(chars) and l == 1:
#             #     p += 1

#             # reset variables
#             cur = chars[i]
#             l = 1

#             if i + 1 == len(chars) and l == 1 and p < len(chars):
#                 chars[p] = cur
#                 p += 1

#     print(chars)
#     return p

# This is the working solution
def foo(chars):
    # Since we're updating the input, we need to keep track of the
    # indexes we're updating
    p = 0

    # we also need to keep track of the length of 
    # consecutive characters
    l = 0

    # start that comparison character at the first
    cur = chars[0]

    # iterate through the characters
    for i in range(len(chars)):
        # if the current character is a match, inc length
        if chars[i] == cur:
            l += 1

        # if we find a new character
        if chars[i] != cur:
            # overwrite the input array with the current
            # char at the pointer, inc pointer
            chars[p] = cur
            p += 1

            # if the length is more than 1 digit, split it apart
            if l > 9:
                splitL = [*str(l)]
                for n in splitL:
                    chars[p] = n
                    p += 1
            # otherwise, add it if greater than 1
            elif l > 1:
                chars[p] = str(l)
                p += 1

            # reset the tracking variables
            # start l at 1 this time because when we first set the cur char,
            # we still had to iterate over that index
            # here, we are moving on to the next one already
            cur = chars[i]
            l = 1
        
        # if we've come across the last character, 
        # there will be no other character to comapre to
        # so we need to repeat the above process
        if i+1 == len(chars):
            chars[p] = cur
            p += 1
            
            if l > 9:
                splitL = [*str(l)]
                for n in splitL:
                    chars[p] = n
                    p += 1
            elif l > 1:
                chars[p] = str(l)
                p += 1

    # print(chars, p)
    return p

print(foo(["a"])) # 1
print(foo(["a", "a"])) # 2
print(foo(["a", "a", "a"])) # 2
print(foo(["a", "a", "b"])) # 3
print(foo(["a","a","b","b","c","c","c"])) # 6
print(foo(["a","b","b","b","b","b","b","b","b","b","b","b","b"])) # 12
# print(foo(['a', 'b', 'c'])) # 3
print(foo(["a","a","a","a","a","b"])) # 3


# Submission:
# Time: 60ms - 70.70%
# Space: 16.8 - 59.88%
# Runtime: best case, O(n) time, I think this is constant in space?