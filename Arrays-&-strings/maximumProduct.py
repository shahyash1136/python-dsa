def maximumProduct(nums: list[int]) -> int:
    nums.sort()
    product_a = nums[-1] * nums[-2] * nums[-3]
    product_b = nums[0] * nums[1] * nums[-1]

    return product_a if product_a > product_b else product_b


nums = [-10, -10, 1, 3, 2]
print(maximumProduct(nums))
