def twoSum(arr,target):
    map = {}
    for i in range(len(arr)):
        compliment = target - arr[i]
        if compliment in map:
            return [map[compliment],i]
        map[arr[i]] = i            


arr = [3,2,4]
target = 6
value = twoSum(arr,target)
print(value)