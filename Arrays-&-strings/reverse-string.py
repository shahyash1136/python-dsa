def reverseString(str):
    char_list = list(str)
    left = 0
    right = len(char_list) - 1
    while left < right:
        char_list[left], char_list[right] = char_list[right], char_list[left]
        left += 1
        right -= 1
    return ''.join(char_list)


str = 'hello'
value = reverseString(str)
print(value)