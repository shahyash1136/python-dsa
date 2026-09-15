def frequencyCounting(s, t):
    dict_char = {}
    for i in range(len(s)):
        dict_char[s[i]] = dict_char.get(s[i], 0) + 1
    for i in range(len(t)):
        dict_char[t[i]] = dict_char.get(t[i],0) - 1

    return all(v == 0 for v in dict_char.values())


s = "anagram"
t = "nagaram"
value = frequencyCounting(s, t)
print(value)
