def moveZeroes(arr):
    slow = 0
    fast = 0
    for _ in range(slow, len(arr)):
        if arr[fast] != 0:
            arr[slow] = arr[fast]
            slow += 1
        fast += 1

    for _ in range(slow, len(arr)):
        arr[slow] = 0
        slow += 1
    return arr


arr = [0, 1, 0, 3, 12]
value = moveZeroes(arr)
print(value)
