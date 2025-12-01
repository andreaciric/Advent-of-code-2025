START_NUMBER = 50
INPUT_FILE = "/Users/andreaciric/Documents/Advent-of-code-2025/day1/input.txt"

def find_most_visited_from_file(start_number, filename):
    current_position = start_number

    password1 = 0
    password2 = 0

    with open(filename, "r") as file:
        for line in file:
            command = line.strip()

            if not command:
                continue        # skip empty lines

            direction = command[0].upper()

            previous_position = current_position

            # if direction == "R":
            #     division, current_position = divmod((current_position + steps), 100)
            #     password2 += division - (previous_position == 0 and division < 0)
            # elif direction == "L":
            #     division, current_position = divmod((current_position - steps), 100)
            #     password2 += abs(division) - (previous_position == 0 and division < 0) + (current_position == 0)
            # else:
            #     raise ValueError(f"Invalid command: {command}! Use L or R.")

            if direction not in ("R", "L"):
                raise ValueError(f"Invalid command: {command}! Use L or R.")
            
            steps = int(command[1:]) * (1 if direction == "R" else -1)

            division, current_position = divmod((current_position + steps), 100)

            password1 += (current_position == 0)
            password2 += abs(division) - (previous_position == 0 and division < 0) + (current_position == 0 and steps < 0)

    return password1, password2

if __name__ == "__main__":
    password1, password2 = find_most_visited_from_file(
        START_NUMBER, INPUT_FILE
    )

    print("PASSWORD 1:", password1)
    print("PASSWORD 2:", password2)