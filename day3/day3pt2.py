import string 

def get_most_common_item(items:str):
    for x in items[0]:
        if x in items[1]:
            if x in items [2]:
                return x

def create_batch(list: list, batch_size: int): 
    return (list[batch:batch + batch_size] for batch in range(0, len(list), 3))

items = []
with open("input.txt", "r") as file: 
    items = file.readlines()

scoring_dict = {}

letters_ordered = [*string.ascii_lowercase, *string.ascii_uppercase]

for priority, letter in enumerate(letters_ordered, start=1):
    scoring_dict[letter] = priority

score = 0

for batch in create_batch(items, 3):
    most_common_item = get_most_common_item(batch)
    score += scoring_dict[most_common_item]

print(score) #2518