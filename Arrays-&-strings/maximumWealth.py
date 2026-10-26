def maximumWealth(accounts: list[list[int]]) -> int:
    best = 0
    for customer in accounts:
        current = 0
        for amount in customer:
            current += amount
        if current > best:
            best = current

    return best

accounts = [[1, 5], [7, 3], [3, 5]]
print(maximumWealth(accounts))

"""
best = 0
loop 1
    current = 0
    loop 1 
        current += amount = 0+1 = 1
    loop 2
        current += amount = 1+5 = 6
    6 > 0
    best = 6

loop 2
    current = 0
    loop 1 
        current += amount = 0+7 = 7
    loop 2
        current += amount = 7+3 = 10
    10 > 6
    best = 10

loop 3
    current = 0
    loop 1 
        current += amount = 0+3 = 3
    loop 2
        current += amount = 3+5 = 8
    8 > 10
    best = 10

return 10
"""
