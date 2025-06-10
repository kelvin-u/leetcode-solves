nums = [100, 4, 200, 1, 3, 2]
output = 4


# convert nums to a set
longest = 0

numSet = set(nums)

for n in numSet:
    # check if it's the start of a sequence if it's left neighbour doesnt exist it's the start
    if (n - 1) not in numSet:
        length = 0
        while n in numSet:
            length += 1
            n += 1
        longest = max(longest, length)
print(longest)
