nums = [1,2,3,1]

# return true if a num is repeated

def containsDuplicate(nums):
    seenSet = set()
    for n in nums: 
        if n in seenSet:
            return True
        seenSet.add(n) 
    return False

print(containsDuplicate(nums))