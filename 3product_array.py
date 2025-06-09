nums = [1,2,3,4]

# [1,2,3,4,5] -> [24,12,8,6]
# [1,1,2,6]
# [24,12,4,1]

output = [0] * len(nums)
prefix = 1

for i in range(len(nums)):
    output[i] = prefix
    prefix *= nums[i]

postfix = 1
for i in range(len(nums)-1, -1, -1): # go backwards start:stop:step
    output[i] *= postfix
    postfix = postfix * nums[i]

print(output)