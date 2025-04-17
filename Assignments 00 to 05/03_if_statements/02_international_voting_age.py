
# Write a program which asks a user for their age and lets them know if they can or can't vote in the following three fictional countries.

# the voting age in Peturksbouipo is 16 
# the voting age in Stanlau is 25
# the voting age in Mayengua is 48 

# Your code should prompt the for their age and print whether or not they can vote in Peturksbouipo, Stanlau, or Mayengua.

# Here's a sample run of the program:

# How old are you? 20 You can vote in Peturksbouipo where the voting age is 16. You cannot vote in Stanlau where the voting age is 25. You cannot vote in Mayengua where the voting age is 48.


# Solution 

voting_age_in_Peturksbouipo = 16
voting_age_in_Stanlau = 25
voting_age_in_Mayengua = 48

def main():
  while True:
    try:
      user_age = int(input("Enter your age: "))
      break
    except ValueError:
      print("Invalid input. Please enter a number.")

  if user_age >= voting_age_in_Peturksbouipo:
    print(f"You can vote in Peturksbouipo, where the voting age is {voting_age_in_Peturksbouipo}.")
  else:
    print(f"You cannot vote in Peturksbouipo, where the voting age is {voting_age_in_Peturksbouipo}.")

  if user_age >= voting_age_in_Stanlau:
    print(f"You can vote in Stanlau, where the voting age is {voting_age_in_Stanlau}.")
  else:
    print(f"You cannot vote in Stanlau, where the voting age is {voting_age_in_Stanlau}.")

  if user_age >= voting_age_in_Mayengua:
    print(f"You can vote in Mayengua, where the voting age is {voting_age_in_Mayengua}.")
  else:
    print(f"You cannot vote in Mayengua, where the voting age is {voting_age_in_Mayengua}.")

if __name__ == "__main__":
  main()