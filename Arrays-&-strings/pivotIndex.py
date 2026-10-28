def pivotIndex(nums: list[int]) -> int:
    total = sum(nums)
    left_sum = 0
    right_sum = 0

    for i in range(len(nums)):
        right_sum = total - left_sum - nums[i]
        if left_sum != right_sum:
            left_sum += nums[i]
        else:
            return i
    return -1


nums = [1, 2, 3]
print(pivotIndex(nums))
"""
right_total = 1 + (-1) = 0
total = 0
index = -1
Loop1 i = 0
    0 == 0 -> True
        index = 0
    total += 2
Loop2 i = 1
    2 == 0 -> False
        index = 0
    total += 3
Loop3 i = 2
    3 == 0 -> False
        index = 0
    total += 2
return 0
"""
