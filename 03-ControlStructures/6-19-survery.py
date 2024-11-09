"""
Prints a survey consisting of three questions. Save the answers to logical type variables.Then view the survey result.

Sample result:
SURVEY Are you interested in computer science? (y/n): y
Do you like playing computer games? (y/n): n
Do you have an Instagram account? (y/n): y

SURVEY RESULTS Interested in computer science: Yes
Playing computer games: No
Has an Instagram account: Yes
"""

science = input("SURVEY Are you interested in computer science? (y/n): ")
games = input("Do you like playing computer games? (y/n): ")
insta = input("Do you have an Instagram account? (y/n): ")

science_bool = True if science == 'y' else False
games_bool = True if games == 'y' else False
insta_bool = True if insta == 'y' else False

science_str = 'Yes' if science_bool else 'No'
games_str = 'Yes' if games_bool else 'No'
insta_str = 'Yes' if insta_bool else 'No'

print(f"""
SURVEY RESULTS
Interested in computer science: {science_str}
Playing computer games: {games_str}
Has an Instagram account: {insta_str}
""")
