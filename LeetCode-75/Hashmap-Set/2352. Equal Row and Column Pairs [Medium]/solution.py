def foo(grid):
    count = 0
    temp = [None] * len(grid)
    rowMap, colMap = {}, {}

    # Get all rows as strings in map and count
    for i in range(len(grid)):
        row = grid[i]
        for j in range(len(row)):
            temp[j] = str(row[j])
        # rowString = ''.join(temp)
        rowString = str(temp)

        if rowString in rowMap:
            rowMap[rowString] += 1
        else:
            rowMap[rowString] = 1

    # same for columns
    for i in range(len(grid[0])):
        for j in range(len(grid)):
            temp[j] = str(grid[j][i])
        # colString = ''.join(temp)
        colString = str(temp)

        if colString in colMap:
            colMap[colString] += 1
        else:
            colMap[colString] = 1

    for s in colMap:
        if s in rowMap:
            count += colMap[s] * rowMap[s]

    return count

print(foo([[3,2,1],[1,7,6],[2,7,7]])) # expect 1
print(foo([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]])) # expect 3
print(foo([[11,1],[1,11]])) # expect 2

# Submission:
# Time: 42ms - 55.52%
# Space: 21.6mb - 62.31%
# Runtime: O(n^2)