# print("Q1")

# def convert_f_to_c(temp_in_farenheit):
    
#    celsiustemp = round((temp_in_farenheit - 32) *  5/9, 1)

#     return celsiustemp

# print(convert_f_to_c(32))

print("Q2")

def calculate_mean(total_sum, num_items):
    mean = total_sum / num_items
    return mean
    print(mean)

random_numbers = [5, 7, 24, 8]

sum_of_random_numbers = sum(random_numbers)

print(calculate_mean(sum_of_random_numbers,len(random_numbers)))

results = calculate_mean(sum_of_random_numbers, len(random_numbers))

print(results)

print("Q3")

import csv
#this will turn the data into a list
colours = []

with open("reading-writing-exercises/exercise_data/colours_20.csv") as csv_file:
    # csv.reader tells the python that what you imported above needs to be used to read the csv file
    reader = csv.reader(csv_file)
    for line in reader:
        colours.append(line[4])

import csv
def read_csv_file(filepath):
    colours = []
    with open(filepath) as csv_file:
        reader = csv.reader(csv_file)
        for line in reader:
            colours.append(line)
        return colours

print(read_csv_file("reading-writing-exercises/exercise_data/colours_20.csv"))