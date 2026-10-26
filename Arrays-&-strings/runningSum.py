def runningSum(nums: list[int]) -> list[int]:
    total = 0
    new_array = []
    for i in range(0, len(nums)):
        total += nums[i]
        new_array.append(total)
    return new_array


def runningSum2(nums: list[int]) -> list[int]:
    total = 0
    for i in range(0, len(nums)):
        total += nums[i]
        nums[i] = total
    return nums


nums = [1, 2, 3, 4]
print(runningSum2(nums))
