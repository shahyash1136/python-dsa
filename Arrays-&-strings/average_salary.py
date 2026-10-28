def average(salary: list[int]) -> float:
    max_salary = salary[0]
    min_salary = salary[0]
    total = 0

    for i in salary:
        if i > max_salary:
            max_salary = i
        elif i != max_salary and i < min_salary:
            min_salary = i
        total += i 

    count = len(salary) - 2
    avg_salary = (total - (max_salary + min_salary)) /  count 

    return avg_salary


salary = [1000, 2000, 3000]
print(average(salary))
"""
max_salary = 1000
min_salary = 1000
total = 0

Loop 1 when i = 0
    if 1000 > 1000 -> False
        max_salary = 1000
    elif 1000 != 1000 and 1000 < 1000 -> False
        min_salary = 1000
    total = 1000

Loop 2 when i = 1
    if 2000 > 1000 -> True
        max_salary = 2000
    total = 3000

Loop 3 when i = 2
    if 3000 > 2000 -> True
        max_salary = 3000
    total = 6000

count = 3 - 2
avg_salary = 6000 - 1000 + 3000 / 1
avg_salary = 2000
"""
