nums = [1, 1, 1, 2, 2, 3]
k = 2


def topKFrequent(nums, k):
    nums_map = {}

    # frequencey counter for all the numbers
    for n in nums:
        nums_map[n] = nums_map.get(n, 0) + 1

    print(nums_map)
    # sort it
    sorted_list = sorted(nums_map.items(), key=lambda x: x[1], reverse=True)

    # return up to k elements
    output = []
    for item in sorted_list[:k]:
        output.append(item[0])

    return output
