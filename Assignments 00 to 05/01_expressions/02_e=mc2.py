
# Write a program that continually reads in mass from the user and then outputs the equivalent energy using Einstein's mass-energy equivalence formula (E stands for energy, m stands for mass, and C is the speed of light:

# E = m * c**2

# You should ask the user for mass (m) in kilograms and use a constant value for the speed of light -- C = 299792458 m/s.

# Here's a sample run of the program (user input is in bold italics):

# Enter kilos of mass: 100

# e = m * C^2...

# m = 100.0 kg

# C = 299792458 m/s

# 8.987551787368176e+18 joules of energy!

# Solution: 

C : int = 299792458  # The speed of light in m/s

def main():
    while True:
        try:
            # Get mass from user input
            mass_in_kg: float = float(input("Enter kilos of mass: "))
            if mass_in_kg < 0:
                print("Mass cannot be negative. Please enter a positive value.")
                continue
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            continue
        break

    # Calculate energy
    # equivalently energy = mass * (C ** 2)
    # using the ** operator to raise C to the power of 2

    energy_in_joules: float = mass_in_kg * (C ** 2)

    # Display work to the user
    print("e = m * C^2...")
    print("m = " + str(mass_in_kg) + " kg")
    print("C = " + str(C) + " m/s")
    
    print(f"e = {energy_in_joules} joules!")


if __name__ == '__main__':
    main()