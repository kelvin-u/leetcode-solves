height = [1, 8, 6, 2, 5, 4, 8, 3, 7, 10]

l = 0
r = len(height) - 1
water = 0 

maxleft = height[l]
maxright = height[r]

while l < r:
    if maxleft <= maxright: # determine which side is the bottle neck
        # left side bottle neck
        l += 1
        maxleft = max(maxleft, height[l])
        water += maxleft - height[l]
    else:
        r -= 1
        maxright = max(maxright, height[r])    
        water += maxright - height[r]
    print(water)