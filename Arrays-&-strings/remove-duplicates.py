def removeDuplicates(arr):
    slow = 0
    fast = 1
    length = 1
    for _ in range(fast, len(arr)):
        if arr[fast] != arr[slow]:
            slow += 1
            length += 1
            arr[slow] = arr[fast]
        fast += 1
    return length


arr = [7, 7, 7, 7]
value = removeDuplicates(arr)
print(value)
