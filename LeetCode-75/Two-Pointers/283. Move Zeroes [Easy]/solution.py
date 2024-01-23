def foo(nums):
    p = 0
    z = 0

    while p < len(nums):

        # if p is not a zero
        if nums[p] != 0:

            # find a zero
            while z < len(nums):
                if nums[z] == 0:
                    break
                z += 1

            # only swap them if the zero is before the p
            if z < len(nums) and nums[z] == 0 and z < p:
                temp = nums[z]
                nums[z] = nums[p]
                nums[p] = temp
                z += 1

        p += 1

    print(nums)

foo([0, 1, 0, 3, 12])
foo([1, 0])
foo([1, 2, 3, 1])

# Submission:
# Time: 123ms - 89.60%
# Space: 18.1mb 56.97%
# Runtime:

def bar(nums):
    l = 0
    for r in range(len(nums)):
        if nums[r]:
            print('swapped', nums[l], nums[r])
            nums[l], nums[r] = nums[r], nums[l]
            l += 1

    print(nums)

bar([1, 2, 0, 3, 4])