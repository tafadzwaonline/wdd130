import math
from datetime import datetime

# Get input from user
width = float(input("Enter the width of the tire in mm: "))
ratio = float(input("Enter the aspect ratio of the tire: "))
diameter = float(input("Enter the diameter of the wheel in inches: "))

# Calculate volume
volume = (math.pi * width * width * ratio * (width * ratio + 2540 * diameter)) / 10000000000

# results
print("The approximate volume is", round(volume, 2), "liters")
print("Tire size:", width, "/", ratio, "R", diameter)

# Get current date
current_date = datetime.now().date()

# Write data to file
with open("volumes.txt", "a") as file:
    file.write(f"{current_date}, {width}, {ratio}, {diameter}, {round(volume, 2)}\n")

print("Thank you for using the tire volume calculator!")
