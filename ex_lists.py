print("Q1")

grocery_items = [
"orange", 
"apple", 
"banana", 
"strawberry", 
"grape", 
"blueberry",
"passionfruit",
 "mango", 
 "kiwifruit"]


grocery_items.append(["carrot", "cauliflower", "pumpkin"])

print(grocery_items[0])

print(grocery_items[2])

print(grocery_items[8])

print(grocery_items[0:3])

print(grocery_items[6:9])

print(grocery_items[-1][-1])

print("Q2")

mailing_list = [
    ["Roary", "roary@moth.catchers"],
    ["Remus", "remus@kapers.dog"],
    ["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
    ["biscuit", "biscuit@whippies.park"],
    ["Rory", "rory@whippies.park"],
]

for item in mailing_list:
    print(f"{item[0]}: {item[1]}")

print ("Q3")

name = input("Please give me three names? ")

list_of_names = name.split()

print(len(list_of_names),list_of_names)

print("Q4")


string = input("Please enter a string. ")

yourlist = string.split()
print(len(yourlist),yourlist)

yourlist = list(string)
print(len(string),list(string))


#This is complete