def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
    # create an array of length n
    res = [None for i in range(len(candies))]

    # default max value to first candy
    max = candies[0]
    
    # iterate through, replace max val as necessary 
    for c in candies:
        if c > max:
            max = c
    
    # iterate through again, 
    # assign boolean if candy + extras is more than max
    for i in range(len(candies)):
        res[i] = candies[i] + extraCandies >= max

    # return the array
    return res
            
# Submission:
# time: 49ms - 27.87%
# space: 17.3mb - 18.11%
# runtime: O(n)