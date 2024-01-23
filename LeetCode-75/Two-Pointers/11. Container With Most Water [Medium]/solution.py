def foo(height):
    maxVol = 0

    l = 0
    r = len(height) - 1

    # continue to move inwards until pointers cross
    while l < r:
        curVol = min(height[l], height[r]) * (r - l)
        if curVol > maxVol:
            maxVol = curVol
        
        # move the smaller (or equal) value
        # now a pointer is always moving
        if height[l] <= height[r]:
            l += 1
        else:
            r -= 1
    
    return maxVol

print(foo([1,1])) # 1
print(foo([1,8,6,2,5,4,8,3,7])) #49


# Submission:
# Time: 502ms - 94.16%
# Space: 29.3mb - 78.18%
# Runtime: O(n)