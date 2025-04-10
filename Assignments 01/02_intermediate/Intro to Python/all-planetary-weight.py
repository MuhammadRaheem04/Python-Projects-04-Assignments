# Milestone #2: Planetary Weight Calculator (Handles any capitalization)

# Dictionary of gravity ratios for each planet
gravity_constants = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Mars": 0.378,
    "Jupiter": 2.36,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.14
}

# Ask user for their Earth weight
earth_weight = float(input("Enter your weight on Earth (kg): "))

# Ask user to enter the name of a planet
planet_input = input("Enter a planet (e.g., Mars): ")

# Normalize input (first letter capital, rest lowercase)
planet = planet_input.capitalize()

# Check if the planet is in the dictionary
if planet in gravity_constants:
    gravity = gravity_constants[planet]
    planet_weight = round(earth_weight * gravity, 2)
    print(f"The equivalent weight on {planet}: {planet_weight} kg")
else:
    print("Invalid planet name. Please enter a valid planet from the solar system.")

