def canPlaceFlowers(flowerbed, n):
    # create a counter to see how many flowers at max we could plant
    counter = 0

    # set up an index for a while loop
    # using a while loop instead of a for secificaky
    # for python in order to incrememnt the counter manually
    i = 0

    # iterate through the length of flowerbed
    while i < len(flowerbed):
        # if we come across an open spot
        if flowerbed[i] == 0:
            # check to see if there is no flower behind or ahead of this position
            if (i - 1 < 0 or flowerbed[i-1] == 0) and (i + 1 >= len(flowerbed) or flowerbed[i+1] == 0):
                # if both spots empty, increment counter
                counter += 1
                # ALSO incrememnt index
                # if the next spot is also open, we want to skip it
                # otherwise we would have neighbors
                i += 1
        # incrememnt index
        i += 1

    # return boolean 
    # It wasn't specified, but I saw no harm in returning
    # if the nmber of flowers we could plant is greater than
    # or equal to the number we want to plant
    return counter >= n

# Submission:
# Time: 131ms - 88.00%
# Space: 17.8mb - 6.06%
# Runtime: O(a)