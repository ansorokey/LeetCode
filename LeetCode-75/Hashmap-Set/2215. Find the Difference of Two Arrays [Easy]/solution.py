def foo(nums1, nums2):
    unique1 = []
    unique2 = []
    set1 = set()
    set2 = set()

    for c in nums1:
        if c not in set1:
            set1.add(c)

    for c in nums2:
        if c not in set2:
            set2.add(c)

    for c in set1:
        if c not in set2:
            unique1.append(c)

    for c in set2:
        if c not in set1:
            unique2.append(c)

    return [unique1, unique2]

print(foo(nums1 = [1,2,3], nums2 = [2,4,6])) # expect [[1,3],[4,6]]
print(foo(nums1 = [1,2,3,3], nums2 = [1,1,2,2])) # expect [[3],[]]

# Submission:
# Time:
# Space:
# Runtime: