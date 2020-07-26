print("Q1")

is_moths_in_house = False

if is_moths_in_house:
    print("Get the moths!")
else:
    print("No threats detected.")

print ("Q2")

is_moths_in_house = False
is_mitch_is_home = True


if is_moths_in_house and is_mitch_is_home:
    print("Hooman! Help me get the moths!")


elif not is_moths_in_house and not is_mitch_is_home:
    print("No threats detected.")   

elif is_moths_in_house and not is_mitch_is_home:
    print("Meoooooooow! Hisssss!")

elif not is_moths_in_house and is_mitch_is_home:
    print("Climb on Mitch. ")


print("Q3")

is_car_detected = False
is_light_colour_red = True
is_light_colour_green = True
is_light_colour_amber = True

if not is_car_detected and is_light_colour_red:
    print("Do nothing")

elif is_car_detected and is_light_colour_red:
    print("Flash")

elif not is_car_detected and is_light_colour_green:
    print("Do nothing")

elif is_car_detected and is_light_colour_green:
    print("Do nothing")

elif not is_car_detected and is_light_colour_amber:
    print("Do nothing")

elif is_car_detected and is_light_colour_amber:
    print("Do nothing")

print("Q4")

safe_to_ride = 120

height_prompt = int(input("Hi, how tall are you? "))

height = height_prompt

if height <= 119:
    print("Sorry not today :(")

else:
    print("Hop on!")

#this is done
