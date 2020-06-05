#
# Dictionary with python
#

# Access all key value pairs of a dictionary

sports = {
    1: "Basketball",
    2: "Skateboard",
    3: "Ping pong"
}

for sport in sports:
    print(str(sport) + ": " + sports[sport])

# Create and access a dictionary based on user input

car_shop = {
    "gas": "Ford Focus",
    "hybrid": "BMW i8",
    "electric": "Tesla Model X"
}

print("")

no_answer = True

while no_answer:
    car_choice = input("What type of car do you prefer: gas, hybrid or electric: ")

    if car_choice.lower() == "gas" or car_choice.lower() == "hybrid" or car_choice.lower() == "electric":
        print("---------------------------------------------------------")
        print("Based on your selection, the following car is recommended")
        print("---------------------------------------------------------")
        print(car_shop[car_choice.lower()])
        no_answer = False
    else:
        print("Try typing in one of the three options provided.")
