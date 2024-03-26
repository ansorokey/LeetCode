class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min, max = float('inf'), float('-inf')
        gdc = 1
        for n in nums:
            if n < min:
                min = n
            if n > max:
                max = n

        for i in range(1, n+1):
            if max % i == 0 and min % i == 0:
                gdc = i

        return gdc


# Submission:
# Time: 40ms - 23.68%
# Space: 11.8mb - 59.94%
# Runtime:
