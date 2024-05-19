# Use list comprehension to open the file and parse through
lines = [line.strip() for line in open("day-10/day-10.txt", "r")]

def get_next_coord(current_coords, prev_coords):
    
    current_char = lines[current_coords[1]][current_coords[0]]
    if current_char == '|':
        # If we are going down
        if prev_coords[1] < current_coords[1]:
            return [current_coords[0], current_coords[1] + 1]
        
        # If we are going up
        return [current_coords[0], current_coords[1] - 1]
    elif current_char == '-':
        # If we are going left to right (->)
        if prev_coords[0] < current_coords[0]:
            return [current_coords[0] + 1, current_coords[1]]
        
        # If we are going right to left (<-)
        return [current_coords[0] - 1, current_coords[1]]
    elif current_char == 'L':
        # If we are coming from above
        if prev_coords[1] < current_coords[1]:
            return [current_coords[0] + 1, current_coords[1]]
        
        # If we are coming from the right
        return [current_coords[0], current_coords[1] - 1]
    elif current_char == 'J':
        # If we are coming from above
        if prev_coords[1] < current_coords[1]:
            return [current_coords[0] - 1, current_coords[1]]
        
        # if we are coming from the left
        return [current_coords[0], current_coords[1] - 1]
    elif current_char == '7':
        # if we came from below
        if prev_coords[1] > current_coords[1]:
            return [current_coords[0] - 1, current_coords[1]]
        
        # If we came from the left
        return [current_coords[0], current_coords[1] + 1]
    elif current_char == 'F':
        # If we came from below
        if prev_coords[1] > current_coords[1]:
            return [current_coords[0] + 1, current_coords[1]]
        
        # If we came from the right
        return [current_coords[0], current_coords[1] + 1]
    else:
        raise Exception("Incorrect character " + current_char + " entered.")
    
def get_starting_coords():
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            
            if char == 'S':
                # Check in each axis and see if the char is valid
                good_coords = [[x, y]]
                # Check top
                if y > 0:
                    if lines[y - 1][x] in {'|', '7', 'F'}:
                        good_coords.append([x, y - 1])
                
                # Check bottom
                if y < len(lines) - 1:
                    if lines[y + 1][x] in {'|', 'L', 'J'}:
                        good_coords.append([x, y + 1])
                
                # Check left
                if x > 0:
                    if lines[y][x - 1] in {'-', 'L', 'F'}:
                        good_coords.append([x - 1, y])
                
                # Check right
                if x < len(lines[0]) - 1:
                    if lines[y][x + 1] in {'-', '7', 'J'}:
                        good_coords.append([x + 1, y])
                
                return good_coords
    
    raise Exception("Cannot find two starting coords for selected location")

# Find the two starting coords
starting_coords = get_starting_coords()
prev_1 = starting_coords[0]
loc_1 = starting_coords[1]
prev_2 = starting_coords[0]
loc_2 = starting_coords[2]
num_steps_1 = 1
num_steps_2 = 1


# Go through until the coords of both locations match
while True:
    
    # Go through 1
    new_1 = get_next_coord(loc_1, prev_1)
    prev_1 = loc_1
    loc_1 = new_1
    
    # Go through 2
    new_2 = get_next_coord(loc_2, prev_2)
    prev_2 = loc_2
    loc_2 = new_2
    
    # Update steps
    num_steps_1 += 1
    num_steps_2 += 1
        
    
    # Check to see if the new points are the same
    if new_1 == new_2:
        print(num_steps_1, num_steps_2)
        break