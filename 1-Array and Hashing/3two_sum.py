nums = [1, 2, 11, 15]
target = 26


def twoSum(nums, target):
    map = {}
    for index, value in enumerate(nums):
        complement = target - value
        if complement in map:
            return [map[complement], index]
        map[value] = index


print(twoSum(nums, target))
