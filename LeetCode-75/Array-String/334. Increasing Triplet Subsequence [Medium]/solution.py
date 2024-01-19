# Brute force loops
# def foo(nums):
#     if len(nums) < 3:
#         return False

#     i = 0
#     smallest = nums[i]
#     while i < len(nums):
#         if nums[i] <= smallest:
#             smallest = nums[i]
#             first = second = nums[i]


#             # find the first larger number
#             for j in range(i+1, len(nums)):
#                 if nums[j] > first:
#                     second = nums[j]
#                     # find the first number larger than b
#                     for k in range(j+1, len(nums)):
#                         if nums[k] > second:
#                             return True
        
#         i += 1
    
#     return False

# increasing min aproaches
"""
In this approach, we're using simple logic.
Instead of constantly looking for the max, we start with the first value.
The we iterate.
Is the next value smaller than the smallest?
If so, we replace them.
If it's not, then it's bigger than the smallest.
Move on.
We only ever need to return true if we find a number that is bigger
than the smallest ANd the next smallest as we go down the line.
"""
def foo(nums):
    # set two variables to a max value that everything will be less than
    first = second = float('inf')

    # iterate through hte nums
    for n in nums:
        # if this num is less than the first, set it as the new
        # first smallest num
        # a first will always be set 
        if n <= first:
            first = n
        # theonly way to reach this condition is if the first is set
        # if this num is smaller or being set for the first time,
        # that means it is further down and larger than the first
        elif n <= second:
            second = n
        # if this num is larger than the last two, we have found
        # a triple order, so we can return true
        else:
            return True

    # if we never returned true, then we never found a triplet
    return False


print(foo([1, 2, 3, 4, 5])) # True
print(foo([5, 4, 3, 2, 1])) # False
print(foo([0, 2, 0, 5, 0, 8])) # True
print(foo([1, 100, 2, 3])) # True
print(foo([2,4,-2,-3])) # False

# Submission:
# Time: 778ms - 95.78%
# Space: 32.5mb - 85.84%
# Runtime: O(n) and soace of O(1)