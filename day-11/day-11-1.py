# Use list comprehension to open the file and parse through
lines = [line.strip() for line in open("day-11/day-11.txt", "r")]

def sign(number: int) -> int:
    '''Returns 1 if the number is positive, -1 if negative, and 0 if 0'''
    if number > 0:
        return 1
    elif number < 0:
        return -1
    else:
        return 0

def calculate_next_coord(current_coords:list[int], destination_coords:list[int]) -> list[int]:
    '''Sees which distance to the coordanite is longer and decides to go that way.
    This will return the value that will lead to the shortest path to the next galaxy'''
    
    distance_in_x = destination_coords[0] - current_coords[0]
    distance_in_y = destination_coords[1] - current_coords[1]
    
    if abs(distance_in_x) > abs(distance_in_y):
        return [current_coords[0] + sign(distance_in_x), current_coords[1]]
    else:
        return [current_coords[0], current_coords[1] + sign(distance_in_y)]

def add_extra_row(array: list[str], row_num: int) -> list[str]:
    '''Will add an extra row above the specified row'''
    
    extra_row = '.' * len(array[0])
    
    array.insert(row_num, extra_row)
    
    return array
    
def add_extra_column(array: list[str], column_num: int) -> list[str]:
    '''Adds an extra comumn after the specified column'''
    
    return_arr = []
    
    for line in array:
        return_arr.append(line[:column_num + 1] + '.' + line[column_num + 1:])
    
    return return_arr

# Add in the extra rows
for i in reversed(range(len(lines))):
    if len(set(lines[i])) == 1:
        lines = add_extra_row(lines, i)

# Add extra columns
for i in reversed(range(len(lines[0]))):
    empty = True
    for j in range(len(lines)):
        if lines[j][i] == "#":
            empty = False
    
    if empty:
        lines = add_extra_column(lines, i)

# Get all star locations
galaxy_coords = []
for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char == '#':
            galaxy_coords.append([j, i])


distances = []
for i, galaxy in enumerate(galaxy_coords):
    other_galaxies = list(galaxy_coords)
    other_galaxies = other_galaxies[i + 1:]

    # Go through each other galaxy and add the distances to the array
    for other in other_galaxies:
        current_coords = galaxy
        num_steps = 0
        # Find the distance
        while True:
            current_coords = calculate_next_coord(current_coords, other)
            num_steps += 1
            
            if current_coords == other:
                distances.append(num_steps)
                break
    


print(sum(distances))