height = [1, 8, 6, 2, 5, 4, 8, 3, 7, 10]

l = 0
r = len(height) - 1
area = 0
while l < r:
    # find the area
    maxArea = (r - l) * min(height[l], height[r])
    area = max(maxArea, area)

    if height[l] > height[r]:
        r -= 1
    else:
        l += 1
print(area)
