# def foo(nums, k):
#     maxavg = float("-inf")

#     # iterate through the array
#     for i in range(0, len(nums)-(k-1)):
#         cursum = 0
#         for j in range(i, i+k):
#             cursum += nums[j]

#         curavg = cursum / k
#         if curavg > maxavg:
#             maxavg = curavg

#     return maxavg

def foo(nums, k):
    start = 0
    end = 0
    cursum = 0
    maxavg = float("-inf")

    while end < len(nums):
        cursum += nums[end]

        # the length will be k, but the difference between 
        # first and last index is k minus one
        if end - start == k-1:
            curavg = cursum / k

            if curavg > maxavg:
                maxavg = curavg
            cursum -= nums[start]
            start += 1

        end += 1

    return maxavg

print(foo([1, 2, 3, 4, 5], 2)) # 4.5
print(foo(nums = [1,12,-5,-6,50,3], k = 4)) # 12.75

# Submission:
# Time: 893ms - 80.11%
# Space: 28.5mb - 63.57%
# Runtime: O(n)