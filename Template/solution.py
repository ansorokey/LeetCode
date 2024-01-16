def gcdOfStrings(str1: str, str2: str) -> str:
    # Find the smaller of the two strings
    smaller = str2
    if len(str1) < len(str2):
        smaller = str1

    # find the bigger of the two strings
    bigger = str1
    if len(str2) > len(str1):
        bigger = str2

    # start with the result being the smaller one
    res = smaller

    # We will take the current result and check to see if it can divide
    # both strings evenly
    # if it cannot, we reduce the length of it until it is an empty string
    while len(res) > 0:
        # to check if it divides evenly, 
        # we can concatenate it t times to see if it
        # reproduces the same string
        # do this to both inputs.
        t1 = len(bigger) // len(res)
        t2 = len(smaller) // len(res)
        if res * t1 == bigger and res * t2 == smaller:
            return res
        
        # reduce result
        res = res[:-1]

    return ""


# Submission:
# time: 41ms - 49.83%
# space: 17.2mb - 47.20%
# runrime: O(min(m, n) * (m+n))