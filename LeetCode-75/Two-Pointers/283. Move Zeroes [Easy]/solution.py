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
foo([0, 0, 0, 0, 0, 1])


# Submission:
# Time: 123ms - 89.60%
# Space: 18.1mb 56.97%
# Runtime: