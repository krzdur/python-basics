"""
Calculates a dog's age in dog's years. For the first two years, a dog's life is equal to 10.5 human years. After that,
each dog year is equal to 4 human years.

Sample result:
Enter the dog's age in human years: 15
The dog's age in dog's years is 73 years.
"""

human_age = int(input("Enter the dog's age in human years: "))
dog_age = 0


if 0 < human_age <= 2:
    dog_age = human_age * 10.5
elif human_age > 2:
    dog_age = int(2 * 10.5 + (human_age - 2) * 4)
else:
    print("Dog's age must be greater than 0")

print(f"The dog's age in dog's years is {dog_age} years.")
