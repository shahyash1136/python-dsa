def dominantIndex(nums: list[int]) -> int:
    mx = float("-inf")
    second_mx = float("-inf")

    for num in nums:
        if num > mx:
            second_mx = mx
            mx = num
        elif num != mx and num > second_mx:
            second_mx = num

    if mx >= second_mx * 2:
        return nums.index(mx)
    return -1


nums = [3, 6, 1, 0]
print(dominantIndex(nums))

"""
[3, 6, 1, 0]
start: mx = -inf, second_mx = -inf
num=3: if True        -> second_mx = -inf, mx = 3
num=6: if True        -> second_mx = 3,    mx = 6
num=1: if False, elif (1 != 6 and 1 > 3) False -> kuch nahi, mx = 6, second_mx = 3
num=0: if False, elif (0 != 6 and 0 > 3) False -> kuch nahi, mx = 6, second_mx = 3
end:   6 >= 3 * 2 -> True -> nums.index(6) = 1

[1, 2, 3, 4]
start: mx = -inf, second_mx = -inf
num=1: if True -> second_mx = -inf, mx = 1
num=2: if True -> second_mx = 1,    mx = 2
num=3: if True -> second_mx = 2,    mx = 3
num=4: if True -> second_mx = 3,    mx = 4
end:   4 >= 3 * 2 -> 4 >= 6 False -> return -1
"""
