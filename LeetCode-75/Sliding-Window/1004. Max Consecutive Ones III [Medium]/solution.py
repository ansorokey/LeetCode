# # One pointer approach, longest subarray as is
# def foo(nums, k):
#     res = 0
#     curCount = 0

#     # iterate through nums
#     for i in range(len(nums)):
#         curNum = nums[i]

#         # if we reached a zero, reset the count
#         if curNum == 0:
#             curCount = 0
#         # otherwise, we found a 1 an we can increase the count
#         else:
#             curCount += 1
#             # we only need to compare max when we find 1s
#             if curCount > res:
#                 res = curCount

#     return res

# Two pointer aproach
def foo(nums, k):
    maxCount = start = end = 0
    flips = k

    while end < len(nums):
        # Is end on a 0 or a 1
        # always decrease flips when landing on a zero
        if nums[end] == 0:
            flips -= 1

        if flips < 0:
            while flips < 0:
                start += 1
                if nums[start - 1] == 0:
                    flips += 1 

        curCount = end - start + 1
        if maxCount < curCount:
            maxCount = curCount

        end += 1

    return maxCount

# print(foo([1, 1, 1], 0)) # expect 3
# print(foo([1, 1, 0], 0)) # expect 2
# print(foo([0, 1, 1], 0)) # expect 2
# print(foo([1, 1, 0], 1)) # expect 3
# print(foo([0, 1, 1], 1)) # expect 3
# print(foo([1, 1, 1, 0, 1, 1, 1, 1], 1)) # test 4, real 8
print(foo(nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2)) # real 6, test 4
print(foo(nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3)) # real 10, test 4
print(foo([0,0,1,1,1,0,0], 0)) # expect 3
print(foo([0, 0, 0, 0], 0))

# Submission:
# Time: 439ms - 75.85%
# Space: 17mb - 87.29%
# Runtime: