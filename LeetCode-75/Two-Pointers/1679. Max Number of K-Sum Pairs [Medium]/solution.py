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
    past = {}

    for i in range(len(nums)):
        cur = nums[i]
        diff = k - cur

        # if we have come across that number before:
        if diff in past:
            # we've found a pair, increment
            res += 1
            # now we can't use that number anymore
            # remove it from the collection
            

        # if this is a new addition
        else:
            past[diff] = i

print(foo(nums = [1,2,3,4], k = 5)) # 2
print(foo([3,1,3,4,3], k = 6)) # 1

# Submission:
# Time:
# Space:
# Runtime: