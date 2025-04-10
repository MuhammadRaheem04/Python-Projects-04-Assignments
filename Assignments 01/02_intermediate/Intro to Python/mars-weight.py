# Milestone #1: Calculate Weight on Mars

# Ask user to enter their weight on Earth
earth_weight = float(input("Enter a weight on Earth (kg): "))

# Mars gravity is 37.8% of Earth's gravity
mars_gravity = 0.378

# Calculate weight on Mars and round to 2 decimal places
mars_weight = round(earth_weight * mars_gravity, 2)

# Show result
print(f"The equivalent weight on Mars: {mars_weight} kg")
