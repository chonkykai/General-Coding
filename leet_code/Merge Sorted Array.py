def merge(nums1, m, nums2, n):
    nums1.sort()
    print(nums1)
    for i in range(m + n):
        if (nums1[i] == 0) and (nums2 != []):
            nums1[i] = nums2[0]
            nums2.pop(0)
    nums1.sort()
    return nums1

print(merge([-1,0,0,3,3,3,0,0,0], 6, [1,2,2], 3))
print(merge([1,2,3,0,0,0], 3, [2,5,6], 3))
print(merge([1], 1, [], 0))
print(merge([0], 0, [1], 1))
print(merge([-1,0,0,3,3,3,0,0,0], 6, [1,2,2], 3))