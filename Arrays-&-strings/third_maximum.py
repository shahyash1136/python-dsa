def thirdMax(nums: list[int]) -> int:
    first = float("-inf")
    second = float("-inf")
    third = float("-inf")

    for x in nums:
        if x > first:
            third = second
            second = first
            first = x
        if x > second and x < first:
            third = second
            second = x
        if x > third and x < first and x < second:
            third = x
    if third == float('-inf'):
        return first 
    return third

nums = [1,2]
print(thirdMax(nums))
