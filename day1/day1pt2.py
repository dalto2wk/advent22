calories_str = []
with open("input.txt", "r") as file: 
    calories_str = file.readlines()

elf_delim = '\n'

cals = []
curr_elf_cal = 0
for index, cal in enumerate(calories_str):
    if cal == elf_delim:
        cals.append(curr_elf_cal)
        curr_elf_cal = 0
        continue
    else:
        cal.replace(elf_delim, "")
        curr_elf_cal += int(cal)

cals.sort(reverse=True)

print(sum(cals[0:3])) ## 197400
