def removeDuplicates(nums: list[int]) -> int:
    slow = 0
    fast = 1
    length = 1
    for i in range(fast,len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            length += 1
            nums[slow] = nums[fast]
        fast +=1
    return length


nums = [1, 1, 2]
values = removeDuplicates(nums)
print(values)
