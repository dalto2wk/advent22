import string 

items = []
with open("input.txt", "r") as file: 
    items = file.readlines()

scoring_dict = {}

print(string.ascii_lowercase)
print(string.ascii_uppercase)