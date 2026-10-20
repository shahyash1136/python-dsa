def findMaxConsecutiveOnes(nums: list[int]) -> int:
    current = 0
    best = 0
    for x in nums:
        if x != 1:
            current = 0
        else:
            current += 1
            if current > best:
                best = current
    return best

    
nums = [1, 0, 1, 1, 0, 1]
print(findMaxConsecutiveOnes(nums))
