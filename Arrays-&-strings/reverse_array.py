def reverse_array(nums):
    l = 0
    r = len(nums) - 1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1

arr = [1, 2, 3, 4, 5]
reverse_array(arr)
print(arr)

""" 
start: l=0, r=4  -> nums[0]=1, nums[4]=5 -> swap -> [5, 2, 3, 4, 1]
l=1, r=3 -> ? -> nums[1]=2, nums[3]=4 -> swap -> [5, 4, 3, 2, 1]
l=2, r=2 -> ? -> loop stops

 """
