nums = [-1, 0, 3, 5, 9, 12]
target = 9


def search(nums, target) -> int:
    l = 0
    r = len(nums) - 1

    while l <= r:
        mid = (l + r) // 2  # -> l + ((r - l) // 2)
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1


search(nums, 9)
