def foo(nums):
    rightSum = 0
    leftSum = 0

    # get the total sum
    for n in nums:
        rightSum += n

    # Now we have the sum of every digit
    # We can begin creating the left sums
    # AND by going the same way, we can just decrement the rightsum by 
    # the current number to see the sum excluding itself

    for i in range(len(nums)):
        if i - 1 >= 0:
            leftSum += nums[i - 1]
        
        rightSum -= nums[i]

        if leftSum == rightSum:
            return i

    return -1

print(foo([1,7,3,6,5,6])) # expect 3

# Submission:
# Time: 121ms - 81.57%
# Space: 17.8mb - 61.70%
# Runtime: O(n)