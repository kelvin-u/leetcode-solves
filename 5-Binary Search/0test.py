def findMedianSortedArrays(nums1, nums2):
    a = nums1
    b = nums2

    if len(a) > len(b):
        a, b = b, a

    l = 0 
    r = len(nums1) - 1
    total_nums = len(a) + len(b)

    half = total_nums // 2
    while True:
        partition_a = (l + r) // 2
        partition_b = half - (partition_a + 1) - 1

        # print(half, partition_a, partition_b)

        # edge case for empty array
        a_left = a[partition_a] if partition_a >= 0 else float('-inf')
        a_right = a[partition_a + 1] if (partition_a + 1) < len(a) else float('-inf') # at least two elements

        b_left = b[partition_b] if partition_b >= 0 else float('-inf')
        b_right = b[partition_b + 1] if (partition_b + 1) < len(b) else float('-inf') # at least two elements

        # print(a_left, b_left)
        # check if correct partition
        if a_left <= b_right and b_left <= a_right:
            # check if even
            if total_nums % 2 == 0: 
                output = (max(a_left, b_left) + min(a_right, b_right)) // 2
            # odd
            else:
                output = min(a_right, b_right) # for odd 1 (1, 2) | (3, 2) 3 4 min is 2
        elif a_left > b_right:
            r = partition_a - l
        else: # b_left > a_right
            l = partition_a + 1


nums1 = [1, 2, 3]
nums2 = [1, 2, 3, 4]
findMedianSortedArrays(nums1,nums2)