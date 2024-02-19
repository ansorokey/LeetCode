def foo(s):
    curNum = []
    curSring = []
    res = []

    nums = set()
    for i in range(10):
        nums.add(str(i))

    for i in range(len(s)):
        c = s[i]
        # print(c)

        if c in nums:
            curNum.append(c)
        elif c == '[':
            res.append(''.join(curNum))
            curNum = []

            res.append(c)
            # print(res)
        elif c == ']':
            j = len(res) - 1
            cat = []
            while res[j] != '[':
                j -= 1
                cat.append(res.pop())
            res.pop()

            toMultiply = ''.join(cat[::-1])
            # print(res)
            lastNum = int(res.pop())
            res.append(lastNum * toMultiply)

        else:
            res.append(c)

        # print(res)

    return ''.join(res)

print(foo('10[a]10[b]10[c]'))