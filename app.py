#
# Dictionary with python
#

# Create and access a dictionary

car_shop = {
    "gas": "Ford Focus",
    "hybrid": "BMW i8",
    "electric": "Tesla Model X"
}

car_choice = input("What type of car do you prefer: gas, hybrid or electric: ")

print("Based on your selection, the following car is recommended")
print("---------------------------------------------------------")
print(car_shop[car_choice])