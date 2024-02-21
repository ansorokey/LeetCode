def rotate(nums, k):
    l = len(nums)
    start = l-k
    stop = start+l

    out = []
    for i in range(start, stop):
        out.append(nums[i%l])

    # out = []
    # save = nums[(start+k) - l]
    # for i in range(start, stop):
    #     nums[(i+k) - l] = nums[i%l]
    #     save = nums[(i+k) - l]

    # print(nums)

print(rotate([1,2,3,4,5,6,7], k = 3))
