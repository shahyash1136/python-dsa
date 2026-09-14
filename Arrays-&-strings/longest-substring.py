def longestString(s):
    char_set = set()
    left = 0
    right = 0
    max_length = 0

    for _ in range(right, len(s)):
        while s[right] in char_set:
            char_set.discard(s[left])
            left += 1
        char_set.add(s[right])
        right += 1
        max_length = max(max_length, right - left)
    return max_length


str = "abcabcbb"
value = longestString(str)
print(value)
