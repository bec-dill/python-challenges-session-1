print("Q1")

names = []

with open("reading-writing-exercises/txt_files/names.txt") as txt_file:
    for line in txt_file:
        line = line.strip()
        names.append(line)
        

print(list(enumerate(names, start=1)))

print("Q2")



with open("reading-writing-exercises/exercise_data/colours_20.csv") as colours_file:
    for column in colours_file:
        # print(colours)

        import csv
#this will turn the data into a list
colours = []

with open("reading-writing-exercises/exercise_data/colours_213.csv") as csv_file:
    #csv.reader tells the python that what you imported above needs to be used to read the csv file
    reader = csv.reader(csv_file)
    for line in reader:
        colours.append(line)

# print(colours)

for colour in colours:

    print(f"{colour[1]} {colour[2]} {colour[4]}")

print("Q3")

import csv
#this will turn the data into a list
colours = []

with open("reading-writing-exercises/exercise_data/colours_213.csv") as csv_file:
    #csv.reader tells the python that what you imported above needs to be used to read the csv file
    reader = csv.reader(csv_file)
    for line in reader:
        colours.append(line[4])

# print(colours)

colour_count = {
    "red": 0,
    "green": 0,
    "blue":0
}

for key in colour_count.keys():
    print(key)
    for colour in colours:
        if key in colour:
            print(colour)
            colour_count[key] += 1

print(colour_count)


# for colour in colours:

#     print(f"{colour[1]} {colour[2]} {colour[4]}")

#this is complete