def removeDuplicates(nums):
    nums[:] = sorted(list(set(nums)))
    return len(nums)

print(removeDuplicates([1,1,1,1,1,1,2]))


# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]