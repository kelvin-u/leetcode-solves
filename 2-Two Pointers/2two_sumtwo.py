nums = [2, 7, 11, 15]
target = 9


def twoSum(nums, target):
    l = 0
    r = len(nums) - 1

    while l < r:
        if nums[l] + nums[r] == target:
            return [l + 1, r + 1]
        if nums[l] + nums[r] > target:
            r -= 1
        if nums[l] + nums[r] < target:
            l += 1


print(twoSum(nums, target))

# pretty simple just l and r pointer if sum is greater than target move r - 1 if less than target l + 1
