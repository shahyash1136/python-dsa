def second_max(nums):
    mx = float("-inf")
    s_max = float("-inf")

    for x in nums:
        if x > mx:
            s_max = mx
            mx = x
        elif x != mx and x > s_max:
            s_max = x

    return s_max if s_max != float("-inf") else None


arr_num = [4]
output = second_max(arr_num)
print(output)
