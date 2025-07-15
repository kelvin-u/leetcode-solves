nums1 = [1, 2, 3]
nums2 = [1, 2, 3, 4, 5]


def findMedianSortedArrays(nums1, nums2):
    a = nums1
    b = nums2

    # we need a to be the shorter array
    if len(a) > len(b):
        a, b = b, a
    l = 0
    r = len(a) - 1

    total_nums = len(a) + len(b)
    half = total_nums // 2

    while True:
        # indicies of where each should be split
        partition_a = (l + r) // 2
        partition_b = half - (partition_a + 1) - 1

        print(partition_a, partition_b)
        a_left = a[partition_a]
        a_right = a[partition_a + 1]

        b_left = b[partition_b]
        b_right = b[partition_b + 1]


findMedianSortedArrays(nums1, nums2)
