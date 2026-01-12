from sample import *

# Container With Most Water
#1. Start two pointers from length and right end.
#2. Move pointer with smaller height as we have chance to move toward bigger height.
#3. Calculate new area and check.
#   if it is greater than max_area, update max_area.
#4. Move pointer until l < r.
#Now, max_area holds the maximum area.

def maxArea(height: list) -> int:
    n = len(height)
    l, r = 0, n - 1
    max_area = 0

    while l < r:  # l <= r is unnecessary as when l=r, area drops to zero which is minimum
        h, w = min(height[l], height[r]), r - l   #height, width of rectangle for area
        area = h * w
        max_area = max(max_area, area)

        #move pointer toward big height
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    
    return max_area

ans1 = maxArea(height1)
print(ans1)
ans2 = maxArea(height2)
print(ans2)