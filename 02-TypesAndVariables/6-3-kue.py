###
# A program that prints a university abbreviation
#   
university = "Krakow University of Economics"

elements = university.split(' ')
elements_w_capital = [e for e in elements if e[0].isupper()]

for ec in elements_w_capital:
    print(ec[0])