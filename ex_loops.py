print ("Q1")

lst = []
x = 0
number = input("enter a number!")
while len(number) > 0:
    if number == "":
        break
    a = int(number)
    x = x + a
    number = input("enter a number!")
print(x)


print ("Q2")



mailing_list = [
["Roary", "roary@moth.catchers"],
["Remus", "remus@kapers.dog"],
["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
["Biscuit", "biscuit@whippies.park"],
["Rory", "rory@whippies.park"],
]

for item in mailing_list:
    print(f"{item[0]}: {item[1]}")

print ("Q3")

names = []

a = input("Enter a name please ")
while len(a) > 0: 
    names.append(a) 
    if a == "":
        break
    a = input("Enter a name please ")
for element in names:
    print(element)

print ("Q4")

groceries = [
    ["Baby Spinach", 2.78],
    ["Hot Chocolate", 3.70],
    ["Crackers", 2.10],
    ["Bacon", 9.00],
    ["Carrots", 0.56],
    ["Oranges", 3.08]
]

new_list = []

for element in groceries:
    print(element[0])
    quan = input("Please tell me how many you would like? ")
    quan = int(quan)
    price = element[1] * quan
    item = element[0]
    new_list.append([item,price])

sum1 = 0

print("====Izzy's Food Emporium====")
for element in new_list:
    print(f"{element[0]:<20} ${element[1]:.2f}")
    sum1 = sum1 + element[1]
print("=============================")
sum1_dollars = "${:.2f}".format(sum1)
sum1_dollars_padded = "{:>27}".format(sum1_dollars)
print(sum1_dollars_padded)

#THIS IS FINISHED



