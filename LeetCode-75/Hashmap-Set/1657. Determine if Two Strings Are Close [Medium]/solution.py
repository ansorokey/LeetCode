# def foo(word1, word2):
#     # are they the same length?
#     if len(word1) != len(word2):
#         return False
    
#     charSet1, charSet2 = {}, {}
#     instanceCount1, instanceCount2 = {}, {}

#     # do they have the same characters?
#     for c in word1:
#         if c not in charSet1:
#             charSet1[c] = 1
#         else:
#             charSet1[c] += 1

#     for c in word2:
#         if c not in charSet2:
#             charSet2[c] = 1
#         else:
#             charSet2[c] += 1

#     for x in charSet1:
#         if x not in charSet2:
#             return False

#         if charSet1[x] not in instanceCount1:
#             instanceCount1[charSet1[x]] = 1
#         else:
#             instanceCount1[charSet1[x]] += 1

#     for x in charSet2:
#         if x not in charSet1:
#             return False
#         if charSet2[x] not in instanceCount2:
#             instanceCount2[charSet2[x]] = 1
#         else:
#             instanceCount2[charSet2[x]] += 1

#     # finally, compare instance counts
#     for y in instanceCount1:
#         if y not in instanceCount2:
#             return False

#         if instanceCount1[y] !=  instanceCount2[y]:
#             return False

#     return True

# same as above, tried removing one for loop
def foo(word1, word2):
    # are they the same length?
    if len(word1) != len(word2):
        return False
    
    charSet1, charSet2 = {}, {}
    instanceCount1, instanceCount2 = {}, {}

    # do they have the same characters?
    for i in range(len(word1)):
        if word1[i] not in charSet1:
            charSet1[word1[i]] = 1
        else:
            charSet1[word1[i]] += 1

        if word2[i] not in charSet2:
            charSet2[word2[i]] = 1
        else:
            charSet2[word2[i]] += 1

    for x in charSet1:
        if x not in charSet2:
            return False

        if charSet1[x] not in instanceCount1:
            instanceCount1[charSet1[x]] = 1
        else:
            instanceCount1[charSet1[x]] += 1

    for x in charSet2:
        if x not in charSet1:
            return False
        if charSet2[x] not in instanceCount2:
            instanceCount2[charSet2[x]] = 1
        else:
            instanceCount2[charSet2[x]] += 1

    # finally, compare instance counts
    for y in instanceCount1:
        if y not in instanceCount2:
            return False

        if instanceCount1[y] !=  instanceCount2[y]:
            return False

    return True
print(foo("aabbcccddd", "abccccdddd"))


# Submission:
# Time: 227ms - 12.62%
# Space: 17.6mb - 94.66%
# Runtime: O(n)