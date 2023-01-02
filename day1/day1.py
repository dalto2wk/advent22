calories_str = []
with open("input.txt", "r") as file: 
    calories_str = file.readlines()

elf_delim = '\n'

max_cal = 0
curr_elf_cal = 0
for index, cal in enumerate(calories_str):
    if cal == elf_delim:
        if curr_elf_cal > max_cal:
            max_cal = curr_elf_cal
        curr_elf_cal = 0
    else:
        cal.replace(elf_delim, "")
        curr_elf_cal += int(cal)

print(max_cal) ## 69206


