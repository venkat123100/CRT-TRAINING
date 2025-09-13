# Input: single line of ages
ages = list(map(int, input().split()))

total_cost = 0
for age in ages:
    if age <= 12:
        total_cost += 100   # child ticket
    elif age < 60:
        total_cost += 150   # adult ticket
    else:
        total_cost += 120   # senior ticket
print(total_cost)
