# testing stuff most water

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

l = 0
r = len(height) - 1
result = 0

while l < r:
    area = (r - l) * min(height[l], height[r])
    result = max(area, result)

    # move pointers based on height

    if height[l] < height[r]:
        l += 1
    else:
        r -= 1
print(result)
