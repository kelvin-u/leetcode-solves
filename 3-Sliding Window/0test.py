height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

l = 0
r = len(height) - 1

leftMax = height[l]
rightMax = height[r]

water = 0

while l < r:
    if leftMax < rightMax: # left side is the bottleneck
        l += 1
        leftMax = max(leftMax, height[l])
        water += leftMax - height[l]
    else:
        r -= 1
        rightMax = max(rightMax, height[r])
        water += rightMax - height[r]
print(water)