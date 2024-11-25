"""
A device in a door registers people entering and leaving a room.The + sign means a person entering a room and the --
sign a person leaving a room. Define the function f(detector) that returns True if at least 3 people were in the room
at the same time, or False otherwise
"""
# INPUT = "+-+++-+---"
INPUT = "+-+-+-+-"
# INPUT = "+-++-+--"
# INPUT = "+-++-++-+---"


def detect(detector):
    people = 0  # Current number of people in room

    for action in detector:
        if action == '+':
            people += 1
            if people >= 3:  # As soon as we reach 3 people, return True
                return True
        elif action == '-':
            people -= 1

    return False


def main():
    print(f'{detect(INPUT)}')


if __name__ == '__main__':
    main()
