# Use list comprehension to open the file and parse through
old_lines = [line.strip() for line in open("day-3/day-3.txt", "r")]
lines = []

# Make lines into 2D array
# This will have two coordanites
for i, line in enumerate(old_lines):
    
    lines.append([])
    
    for j, char in enumerate(line):
        lines[i].append(char)


def find_if_works(x_coord, y_coord, num_digits):
    
    number = ''
    for i in range(num_digits):
        number += lines[y_coord][x_coord + i]
    # print(number + '-' + str(x_coord) + '-' + str(y_coord) + '-' + str(num_digits))
    number = int(number)
    
    # Find possible coordanites for characters around the number
    possible_coords = []
    for y in range(y_coord - 1, y_coord + 2):
        for x in range(x_coord - 1, x_coord + num_digits + 1):
            if x >= 0 and y >= 0 and x < len(lines[0]) and y < len(lines):
                possible_coords += lines[y][x]
    
    # Go through and remove all other characters
    for i in reversed(range(len(possible_coords))):
        bad_strings = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.'}
        if possible_coords[i] in bad_strings:
            possible_coords.pop(i)
    
    
    if len(possible_coords) > 0:
        return number
    else:
        return 0
            

sum_of_numbers = 0
current_number = ''
# Go through each number and add the ones that work
for y, line in enumerate(lines):
    for x, number in enumerate(line):
        if number in {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}:
            current_number += number
        elif len(current_number) > 0:
            # print(x - len(current_number))
            # print(y)
            # print(len(current_number))
            # print(current_number)
            # print("--")
            sum_of_numbers += find_if_works(x - len(current_number), y, len(current_number))
            current_number = ''
    # Account for numbers at the end of the strings
    if len(current_number) > 0:
        sum_of_numbers += find_if_works(len(line) - len(current_number), y, len(current_number))
        current_number = ''

print(sum_of_numbers)