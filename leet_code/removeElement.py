def removeElement(nums, val):
    count = 0
    for i in range(len(nums)):
        if nums[i] == val:
            nums[i] = 100
            count+=1
    nums[:] = sorted(nums)
    return len(nums) - count



print(removeElement([0,1,2,2,3,0,4,2], 2))
# print(removeElement([3,2,2,3], 3))