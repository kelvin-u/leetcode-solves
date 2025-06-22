height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

def trap(height):
    l = 0
    r = len(height) - 1
    leftMax = height[l]
    rightMax = height[r]

    water = 0

    while l < r:
        if leftMax <= rightMax:  # shift left max
            l += 1
            leftMax = max(leftMax, height[l])
            water += leftMax - height[l]
        else:  # shift right max
            r -= 1
            rightMax = max(rightMax, height[r])
            water += rightMax - height[r]
    return water

trap(height)
