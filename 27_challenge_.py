

            
records = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    records.append([name, score])

# find unique scores
# set {} comprehention for unique values
scores = list({s[1] for s in records})
scores.sort()

second_lowest = scores[1]

names = list(map(
    lambda grade: grade[0] if grade[1] == second_lowest else "",
    records
))
      
names.sort()

for name in names:
    if name:
        print(name)

# results = list(filter(
#     lambda grade: grade if grade[1] == second_lowest else False,
#     records
# ))

# names = list(map(lambda grade: grade[0], results))
# names.sort()


for name in names:
    print(name)
    



