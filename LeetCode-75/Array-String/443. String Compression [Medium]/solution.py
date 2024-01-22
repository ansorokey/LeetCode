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

# print(foo(["a"])) # 1
# print(foo(["a", "a"])) # 2
# print(foo(["a", "a", "a"])) # 2
# print(foo(["a", "a", "b"])) # 3
# print(foo(["a","a","b","b","c","c","c"])) # 6
# print(foo(["a","b","b","b","b","b","b","b","b","b","b","b","b"])) # 12
# print(foo(['a', 'b', 'c'])) # 3
# print(foo(["a","a","a","a","a","b"])) # 3


# Submission:
# Time:
# Space:
# Runtime: