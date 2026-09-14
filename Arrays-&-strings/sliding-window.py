def slidingWindow(arr, k):
    start = 0
    end = k - 1
    sum = 0
    for i in range(start, end + 1):
        sum += arr[i]

    max_sum = sum
    while end < len(arr) - 1:
        start += 1
        end += 1
        sum = sum - arr[start - 1] + arr[end]
        max_sum = max(max_sum, sum)

    return max_sum


arr = [2, 1, 5, 1, 3, 2]
k = 3
values = slidingWindow(arr, k)
print(values)
