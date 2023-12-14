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
    
def get_starting_coords(lines):
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

def replace_s_char(maze: list[str], char: str) -> list[str]:
    '''Replaces the S character with the proper character'''
    
    char_coords = get_starting_coords(maze)[1:]
    s_coord = get_starting_coords(maze)[0]
    c1 = char_coords[0]
    c2 = char_coords[1]
    
    maze[s_coord[1]] = maze[s_coord[1]][:s_coord[0]] + char + maze[s_coord[1]][s_coord[0] + 1:]
    
    return maze
    

def get_maze(maze: list[str]) -> list[str]:
    '''Returns just an array of the maze and dots, no other extra pieces'''
    
    # Generate default map
    maze_line = '.' * len(lines[0])
    maze_map = [maze_line] * len(lines)
    
    prev_coords = get_starting_coords(maze)[0]
    coords = get_starting_coords(maze)[1]

    
    while True:
        maze_map[coords[1]] = maze_map[coords[1]][:coords[0]] + maze[coords[1]][coords[0]] + maze_map[coords[1]][coords[0] + 1:]
        # Traverse one character through the maze
        
        temp = coords
        coords = get_next_coord(coords, prev_coords)
        prev_coords = temp
        
        if (maze[coords[1]][coords[0]] == 'S'):
            maze_map[coords[1]] = maze_map[coords[1]][:coords[0]] + maze[coords[1]][coords[0]] + maze_map[coords[1]][coords[0] + 1:]
            break
    
    return maze_map
    
    

lines = get_maze(lines)
lines = replace_s_char(lines, 'J')

def get_num_inside(line: str) -> int:
    '''Input a row and this returns the number of spaces inside'''
    
    inside = False
    num_inside = 0
    prev_corner = ''
    
    for i, pipe in enumerate(line):
        if pipe in {'|'}:
            inside = not inside
        elif pipe == '.' and inside:
            print(line)
            num_inside += 1
        elif pipe in {'F', 'L'}:
            prev_corner = pipe
        elif pipe == '7' and prev_corner == 'L':
            inside = not inside
        elif pipe == 'J' and prev_corner == 'F':
            inside = not inside
        
    return num_inside


sum_inside = 0
for line in lines:
    sum_inside += get_num_inside(line)

print(sum_inside)