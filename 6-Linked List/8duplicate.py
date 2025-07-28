nums = [3, 1, 3, 4, 2]

slow = 0
fast = 0

while True:
    slow = nums[slow]
    fast = nums[nums[fast]]

    if slow == fast:
        break

# now slow == fast

# slow2 = 0

# while True:
#     slow = nums[slow]
#     slow2 = nums[slow2]

#     if slow == slow2:
#         break
# print(slow)
