matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 16

[1, 3, 5, 7, 10, 11, 16, 20, 23, 30, 34, 60]


def searchMatrix(matrix, target) -> bool:
    rows = len(matrix)
    cols = len(matrix[0])

    total_nums = rows * cols
    l = 0
    r = total_nums - 1

    while l <= r:
        mid = (l + r) // 2
        # 1D index to 2D coordinates
        i = mid // cols
        j = mid % cols
        mid_val = matrix[i][j]

        if mid_val == target:
            return True
        elif mid_val < target:
            l = mid + 1
        else:
            r = mid - 1
    return False


print(searchMatrix(matrix, target))
