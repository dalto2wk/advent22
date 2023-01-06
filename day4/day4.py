
items = []
with open("input.txt", "r") as file: 
    items = file.readlines()

count = 0
for x in items: 
    assignments = x.split(',')
    a1 = assignments[0].split('-')
    a2 = assignments[1].split('-')

    if (int(a1[0]) <= int(a2[0]) and int(a1[1]) >= int(a2[1])) or (int(a1[0]) >= int(a2[0]) and int(a1[1]) <= int(a2[1])):
        count += 1
    
print(count) #542
