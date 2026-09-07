"""Input: numbers = [2, 7, 11, 15], target = 9
Output: [1, 2]
(kyunki numbers[0] + numbers[1] = 2 + 7 = 9, aur 1-indexed = [1, 2])"""


def two_sum(arr, target):
    left = 0
    right = len(arr) - 1
    while left != right:
        sum = arr[left] + arr[right]
        if sum == target:
            return [left + 1, right + 1]
        elif sum > target:
            right -= 1
        elif sum < target:
            left += 1


arry = [2, 2, 3, 4]
target = 4
values = two_sum(arry, target)
print(values)
