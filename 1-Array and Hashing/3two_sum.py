nums = [2, 7, 11, 15]
target = 9

def twoSum(nums, target):
    num_map = {}
    for index, value in enumerate(nums):
        complement = target - value
        if complement in num_map:
            return [index, num_map[complement]]
        num_map[value] = index
    

print(twoSum(nums,9))