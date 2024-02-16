def foo(s):
    numStack = []
    stringStack = []
    curNum = []
    curString = []
    res = []
    prefix = []
    
    # since numbers can be greater than 9, we need some way of concatenating multidigit numbers
    # let's make a set of digits as strings, since we cant check the int() of a character
    nums = set()
    for i in range(9):
        nums.add(str(i))

    # iterate through input
    for c in s:
        if c in nums:
            curNum.append(c)
        elif c == '[':
            # start of a new set
            # reset current string and current number
            numStack.append(int(''.join(curNum)))
            curNum = []

            if len(curString) > 0:
                prefix.append(''.join(curString))
                curString = []
            else:
                pass

        elif c == ']': # end of a set
            # Number to multiply, default to 1
            lastum = 1
            if len(numStack) > 0:
                lastNum = numStack.pop()
            
            # string to multiply, can be current set contents or the last string
            toMultiply = ''
            if len(curString) > 0:
                toMultiply = ''.join(curString)
            else:
                # toMultiply = ''.join(res)
                # res = []
                toMultiply = res.pop()

            newString = lastNum * toMultiply

            if len(prefix) > 0:
                newString = prefix.pop() + newString

            # print(newString)
            res.append(newString)
            print(res)

            curString = []
        else:
            curString.append(c)
        
        # print(res)

    if len(curString):
        res.append(''.join(curString))

    return ''.join(res)
        
# "3[a]2[bc]"
# "3[a2[c]]"
# "2[abc]3[cd]ef"
# "abc3[cd]xyz"
# print(foo('a2[b]'))
# print(foo('3[ab]'))
# print(foo('2[a]2[b]'))
# print(foo("3[a2[c]]"))
# print(foo("abc3[de]xyz"))
# print(foo('3[2[a]2[b]]'))
# print(foo("3[z]2[2[y]pq4[2[jk]e1[f]]]ef"))
print(foo('2[jk]e1[f]'))
print(foo('pq4[2[jk]e1[f]]'))
# Submission:
# Time:
# Space:
# Runtime: