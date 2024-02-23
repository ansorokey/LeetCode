class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        last_alt = 0
        max_alt = 0

        for i in range(len(gain)):
            new_alt = last_alt + gain[i]
            if new_alt > max_alt:
                max_alt = new_alt
            last_alt = new_alt

        return max_alt
