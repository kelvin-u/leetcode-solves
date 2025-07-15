nums = [1, 2, 3, 4, 5]


def findMin(nums):
    l = 0 
    r = len(nums) - 1

    while l < r:
        mid = (l+r)//2

        if nums[mid] <= nums[r]:
            r = mid
        else:
            l = mid + 1

    return nums[l]

