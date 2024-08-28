def check_valid_combination(springs, groups) -> bool:
    checked_groups = []
    on_group = False

    for i, char in enumerate(springs):
        if char == "#":
            if not on_group:
                checked_groups.append(1)
                on_group = True
            else:
                checked_groups[-1] += 1
        else:
            on_group = False

    return checked_groups == groups


def find_solutions(springs, groups):

    # Index of the first unknown value
    first_unknown = springs.find("?")

    if first_unknown == -1:
        # Stop the recursion and return if it works
        return check_valid_combination(springs, groups)

    # Return for both the different combinations for this unknown value
    combo_one = springs[:first_unknown] + "." + springs[first_unknown + 1:]
    combo_two = springs[:first_unknown] + "#" + springs[first_unknown + 1:]

    return find_solutions(combo_one, groups) + find_solutions(combo_two, groups)


# Open input.txt and parse the file into an array of lines
with open("input.txt", "r") as file:
    lines = [line.strip() for line in file]

all_combos = 0

for line in lines:
    springs = line[:line.find(" ")]

    groups = line[line.find(" ") + 1:].split(",")
    groups = [int(group) for group in groups]

    all_combos += find_solutions(springs, groups)

print(all_combos)