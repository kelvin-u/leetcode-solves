height = [1, 8, 6, 2, 5, 4, 8, 3, 7]


def maxArea(height):
    result = 0
    l = 0
    r = len(height) - 1

    while l < r:
        # area is length * width
        area = (r - l) * min(height[l], height[r])
        result = max(area, result)

        # move the pointers
        if height[l] > height[r]:
            r -= 1
        else:
            l += 1
    return result

print(maxArea(height))
