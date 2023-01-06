
items = []
with open("input.txt", "r") as file: 
    items = file.readlines()

count = 0
for x in items: 
    assignments = x.split(',')
    a1 = assignments[0].split('-')
    a2 = assignments[1].split('-')

    set1 = { i for i in range(int(a1[0]), int(a1[1]) +1)}
    set2 = { i for i in range(int(a2[0]), int(a2[1]) +1)}
    
    if set1.issubset(set2) or set2.issubset(set1) or not set1.isdisjoint(set2) or not set2.isdisjoint(set1):
        count +=1
    
print(count) #542