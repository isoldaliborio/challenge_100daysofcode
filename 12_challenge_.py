for _ in range(int(input())):
    records = []
    name = input()
    score = float(input())
    records.append([name, score])
    score = (sorted(score, key = lambda x: x[1]))
    m = min(score)
    for record in records:
        if m in records:
            records.remove(m)
    print(min(records))
        

# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39