class RecentCounter:

    def __init__(self):
        # keep track of all pings made to this instance in a queue
        self.pings = []

    def ping(self, t: int) -> int:
        # Add crrent ping to clas queue
        self.pings.append(t)
        
        # this class only cares about pings within range,
        # so we can remove from the instance earliest pings outside that range
        while self.pings[0] < t - 3000:
            self.pings.pop([0])
        
        # now, the number of pings in range is just the length of the list
        return len(self.pings)


# Submission:
# Time: 202ms - 44.50%
# Space: 22.4mb - 50.41%
# Runtime: O(n)?