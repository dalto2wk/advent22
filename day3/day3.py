import string 

def get_letter_in_both_compartments(item: str):
    item_length = int(len(item)/2)
    first_compartment = item[0:item_length]
    second_compartment = item[item_length:]

    for x in first_compartment:
        if x in second_compartment:
            return x


items = []
with open("input.txt", "r") as file: 
    items = file.readlines()

scoring_dict = {}

letters_ordered = [*string.ascii_lowercase, *string.ascii_uppercase]

for priority, letter in enumerate(letters_ordered, start=1):
    scoring_dict[letter] = priority



score = 0
for item in items: 
    letter_in_both_compartments = get_letter_in_both_compartments(item)
    score += scoring_dict[letter_in_both_compartments]


print(score) # 8018