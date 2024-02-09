def foo(asteroids):
    res = []

    for cur in asteroids:
        # grab the last asteroid
        last = None
        if len(res) > 0:
            last = res.pop()

        # are we colliding?
        if (last != None and last > 0) and cur < 0:
            survivor = None
            while (cur != None and last != None and last > 0) and cur < 0:
                print(res, last, cur)
                # last survives
                if cur * -1 > last:
                    survivor = cur
                    if len(res) > 0:
                        last = res.pop()
                    else:
                        last = None

                # cur survices
                elif cur * -1 < last:
                    survivor = last
                    last = None

                else:
                    # neither survive
                    # none added
                    # AND we lose our current asteroid, 
                    # so we can't check for collision
                    cur = None
                    survivor = None
                    if len(res) > 0:
                        last = res.pop()
                    else:
                        last = None

            # if we are here, there might still be a last asteroid
            # we need to add that
            if last != None:
                res.append(last)

            # done looping, add in the survivor if there
            if survivor != None:
                res.append(survivor)

        # no collision
        # can add last and cur
        else:
            if last != None:
                res.append(last)
            res.append(cur)

    return res

# print(foo([-2,-2,1,-2])) # expect [-2, -2, -2]
# print(foo([5, 4, 3, 2, 1, -10])) # exect 10
# print(foo([5, 10, -5]))
# print(foo([-2, 1, 1, -1]))
print(foo([-2,2,1,-2])) # expect [-2]

# Submission:
# Time: 85ms - 59.18%
# Space: 17.9mb - 58.85%
# Runtime: O(n)