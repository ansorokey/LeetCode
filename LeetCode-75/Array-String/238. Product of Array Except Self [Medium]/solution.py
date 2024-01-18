#Brute force, fails constraints.
# def foo(nums):
#     # list of length n
#     res = [None for n in nums]

#     for i in range(len(nums)):
#         running = 1
#         for j in range(len(nums)):
#             if j != i:
#                 running *= nums[j]
#         res[i] = running
#         running = 1
#     return res

# print(foo([1, 2, 3, 4])) # [24, 12, 8, 6]

def bar(nums):
    res = [1 for n in nums]

    running = 1
    for i in range(len(nums)):
        if i - 1 >= 0:
            running *= nums[i-1]
            res[i] = running

    res2 = [1 for n in nums]
    running = 1
    for i in range(len(nums) -1, -1, -1):
        if i + 1 < len(nums):
            running *= nums[i+1]
            res2[i] = running

    for i in range(len(res)):
        res[i] *= res2[i]

    return res

# print(bar([1, 2, 3, 4]))

# Submission:
# Time: 168ms - 80.01%
# Space: 24.9mb - 29.12%
# Runtime: O(n)

def foobar(nums):
    res = [1 for n in nums]

    running = 1
    for i in range(len(nums)):
        if i - 1 >= 0:
            running *= nums[i-1]
            res[i] = running

    running = 1
    for i in range(len(nums) -1, -1, -1):
        if i + 1 < len(nums):
            running *= nums[i+1]
            res[i] *= running

    return res

print(foobar([1, 2, 3, 4]))

# Submission:
# Time: 174ms - 70.37%
# Space: 24.3mb - 66.60%
# Runtime: O(n)
# Space: O(1)?