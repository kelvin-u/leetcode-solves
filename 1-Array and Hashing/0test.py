import sys

nums = [100, 4, 200, 1, 3, 2]
output = 4

# 

nums_set = set(nums)

longest = 0
for n in nums_set:
    if n - 1 not in nums_set:
        length = 0
        while n in nums_set:
            n += 1
            length += 1
        longest = max(longest, length)
print(longest)
