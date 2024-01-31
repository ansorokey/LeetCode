# def foo(nums, k):
#     res = 0

#     for i in range(len(nums)):
#         cur = nums[i]
#         for j in range(i+1, len(nums)):
#             partner = nums[j]
#             if cur + partner == k:
#                 res += 1
#                 break

#     return res

def foo(nums, k):
    res = 0
    # the numbers we passed while iterating
    past = {}

    for i in range(len(nums)):
        cur = nums[i]
        diff = k - cur

        # if we have come across that number before AND
        # if there is at least one of those numbers
        if diff in past and past[diff] > 0:
            # we've found a pair, increment
            res += 1
            # now we can't use that number anymore
            # decrease it's count by one
            past[diff] -= 1
        else:
            # if we've seen this number before, incrememnt it
            if cur in past:
                past[cur] += 1
            else:
                # if we haven't seen that number, count this instance
                past[cur] = 1
        
        # print(past)

    return res

print(foo(nums = [1,2,3,4], k = 5)) # 2
print(foo([3,1,3,4,3], k = 6)) # 1
print(foo([2, 2, 4, 4], k = 6)) #2

# Submission:
# Time: 496ms - 74.58%
# Space: 29.7mb - 29.95%
# Runtime: O(n)