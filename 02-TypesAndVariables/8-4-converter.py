###
# A program that prints your height both in cm and in feet and inches.
#
cm = 170

# calculate the number of feet
total_inches = cm / 2.54

feet = int(total_inches / 12)
inches = int(total_inches % 12)


print(f'I am {cm}cm tall, i.e. {feet} feet and {inches} inches')
