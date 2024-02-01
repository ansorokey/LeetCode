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
    # start all pointers at the beginning of the array
    # start the biggest length at 0
    maxCount = start = end = 0
    # I guess we could just modify the original input, it's just a primitive
    # BUT I don't really like to modify inuts if I dont have to
    flips = k

    # iterate through the array
    while end < len(nums):

        # instead of accounting for if we ave flps or not,
        # just always decrease flips when landing on a zero
        if nums[end] == 0:
            flips -= 1
            
        # Now, we can make those used flips up
        # all we have to do is get back to zero
        # which will also make up for if we were never given any flips to begin with
        while flips < 0:
            start += 1
            if nums[start - 1] == 0:
                flips += 1 
        # since end and start began at the same index, we dont have to worry about
        # checkibg if start is stuck on a zero or not
        # end will have been everything that start could be
        # so any potential 0s ecountered will always push start forwards

        # at this point, start may be ahead of end, which is actually okay!
        # Since we'd get a negative result, it wont ever override the max anyway
        curCount = end - start + 1
        if maxCount < curCount:
            maxCount = curCount

        # advance the end forward
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