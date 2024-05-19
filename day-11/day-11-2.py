# Use list comprehension to open the file and parse through
lines = [line.strip() for line in open("day-11/day-11.txt", "r")]
NUM_EXPANSIONS = 1000000 - 1
def sign(number: int) -> int:
    '''Returns 1 if the number is positive, -1 if negative, and 0 if 0'''
    if number > 0:
        return 1
    elif number < 0:
        return -1
    else:
        return 0

def calculate_distance(expansions: list[list[int]], current_coords: list[int], destination_coords: list[int]) -> int:
    '''Returns the distance to the two galaxies'''
    
    distance_in_x = abs(destination_coords[0] - current_coords[0])
    distance_in_y = abs(destination_coords[1] - current_coords[1])
    
    # Calculate expansions for x coords
    for expansion in expansions[0]:
        if current_coords[0] < expansion and destination_coords[0] > expansion:
            distance_in_x += NUM_EXPANSIONS
            
        if current_coords[0] > expansion and destination_coords[0] < expansion:
            distance_in_x += NUM_EXPANSIONS
    
    # Calculate expansions for y coords
    for expansion in expansions[1]:
        if current_coords[1] < expansion and destination_coords[1] > expansion:
            distance_in_y += NUM_EXPANSIONS
        
        if current_coords[1] > expansion and destination_coords[1] < expansion:
            distance_in_y += NUM_EXPANSIONS
    
    return distance_in_x + distance_in_y

def add_extra_rows(expansion_array: list[list[int]], row_num: int) -> list[list[int]]:
    '''Adds an expansion coordanite to the passed in array.
    Returns the updated expansion array'''
    
    expansion_array[1].append(row_num)
    
    return expansion_array
    
def add_extra_columns(expansion_array: list[list[int]], row_num: int) -> list[list[int]]:
    '''Adds an expansion coordanite to the passed in array.
    Returns the updated expansion array'''
    
    expansion_array[0].append(row_num)
    
    return expansion_array

# Add to the expansions array
expansions = [[], []]

for i in reversed(range(len(lines))):
    if len(set(lines[i])) == 1:
        expansions = add_extra_rows(expansions, i)
        
for i in reversed(range(len(lines[0]))):
    empty = True
    for j in range(len(lines)):
        if lines[j][i] == "#":
            empty = False
    
    if empty:
        expansions = add_extra_columns(expansions, i)

print(expansions)

# Get all star locations
galaxy_coords = []
for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char == '#':
            galaxy_coords.append([j, i])


distances = []
for i, galaxy in enumerate(galaxy_coords):
    
    # print("New galaxy being searched")
    
    other_galaxies = list(galaxy_coords)
    other_galaxies = other_galaxies[i + 1:]

    # Go through each other galaxy and add the distances to the array
    for other in other_galaxies:
        current_coords = galaxy
        distances.append(calculate_distance(expansions, galaxy, other))
    
print(sum(distances))