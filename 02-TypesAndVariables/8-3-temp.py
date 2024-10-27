###
# A program that reads temperature in degrees Celsius from the keyboard.
#

# take input
temp_celsius = float(input("Enter the temperature in Celsius: "))

# convert to kelving
temp_kelvin = temp_celsius + 273.15

# convert to fahrenheit
temp_fahrenheit = temp_celsius * (9/5) + 32

# print the results
print(f"""
Your temperature in Kelvin: {round(temp_kelvin, 2)}
Your temperature in Fahrenheit: {round(temp_fahrenheit, 2)} 
""")