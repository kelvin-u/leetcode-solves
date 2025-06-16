nums = [-4, 0, 1, 2, -1, -4]

# [-4, -1, -1, 0, 1, 5]


def threeSum(nums):
    result = []
    nums.sort()  # sort the input array in place

    for i, a in enumerate(nums):
        # check if the element is the same as before
        if a == nums[i - 1] and i > 0:
            continue
        l = i + 1
        r = len(nums) - 1
        breakpoint()
        while l < r:
            threeSum = a + nums[l] + nums[r]

            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1
            else:
                result.append([a, nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
    return result


print(threeSum(nums))
