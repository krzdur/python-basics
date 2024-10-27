###
# A program that prints a numerical representation of each letter of your name.
#
name = 'Krzysztof' # replace John with your name
name_split = list(name)

for l in name_split:
    print(f'The letter {l} has a code {ord(l)}')