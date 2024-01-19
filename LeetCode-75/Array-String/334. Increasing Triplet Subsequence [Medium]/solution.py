def foo(nums):
    if len(nums) < 3:
        return False

    i = 0
    while i < len(nums):
        j = i
        a = b = c = nums[i]

        # find the first larger number
        for x in range(i+1, len(nums)):
            if nums[x] > a:
                b = nums[x]
                j = x
                break
        
        # find the first number larger than b
        for y in range(j+1, len(nums)):
            if nums[y] > b:
                return True
        
        i += 1
    
    return False

print(foo([1, 2, 3, 4, 5])) # True
print(foo([5, 4, 3, 2, 1])) # False
print(foo([0, 2, 0, 5, 0, 8])) # True
print(foo([1, 100, 2, 3])) # True

# Submission:
# Time:
# Space:
# Runtime: