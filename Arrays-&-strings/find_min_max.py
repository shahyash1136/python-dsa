def find_min_max(nums):
    mx = nums[0]
    mn = nums[0]

    for x in nums:
        if x > mx:
            mx = x
        if x < mn:
            mn = x

    return [mn, mx]


arr_num = [4, 9, 2, 7, 5]
output = find_min_max(arr_num)
print(output)


""" 
mx = nums[0] = 4
mn = nums[0] = 4

loop start
x = 4
    4 > 4 -> False mx = 4
    4 < 4 -> False mn = 4

x = 9
    9 > 4 -> True mx = 9
    9 < 4 -> False mn = 4

x = 2
    2 > 9 -> False mx = 9
    2 < 4 -> True mn = 2

x = 7
    7 > 9 -> False mx = 9
    7 < 2 -> False mn = 2

x = 5
    5 > 9 -> False mx = 9
    5 < 2 -> False mn = 2
"""
