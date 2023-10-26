class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
#       Python does not have an array constructor, so we can instead create an array of m+n none elements
#       Dont forget that python doesn't use declaration keywords (let, const)
        output = [None] * (m+n)

        p1 = 0
        p2 = 0
        cur = 0

        while p1 < m or p2 < n:
            if p1 >= m and p2 < n:
                output[cur] = nums2[p2]
                p2 += 1
            elif p2 >= n and p1 < m:
                output[cur] = nums1[p1]
                p1 += 1
            else:
                if nums1[p1] > nums2[p2]:
                    output[cur] = nums2[p2]
                    p2 += 1
                else:
                    output[cur] = nums1[p1]
                    p1 += 1
            cur += 1

        for i in range(len(nums1)):
            nums1[i] = output[i]
