import math

lines = [line.strip() for line in open("day-8/day-8.txt", "r")]

directions = lines[0]
lines = lines[2:]

maps = []
for line in lines:
    single_map = []
    line = line.split(" = ")
    single_map.append(line[0])
    single_map.append(line[1].replace("(", "").replace(")", "").split(", "))
    maps.append(single_map)
    
starting_maps = []
for i, single_map in enumerate(maps):
    if single_map[0][2] == 'A':
        starting_maps.append(single_map)


def get_next_loc(direction, current_index) -> int:
    current_map = maps[current_index]
    end_loc = '000'
    if direction == 'L':
        end_loc = current_map[1][0]
    elif direction == 'R':
        end_loc = current_map[1][1]
    
    # Find the location we want
    for i, single_map in enumerate(maps):
        if single_map[0] == end_loc:
            return i
            break
    
    return -1

def solve_for_map(map):
    current_direction_index = 0
    current_map_index = maps.index(map)
    num_steps = 0
    while True:
        current_direction = directions[current_direction_index]
        next_index = get_next_loc(current_direction, current_map_index)
        next_map = maps[next_index]
        
        # Update variables
        num_steps += 1
        current_map_index = next_index
        if current_direction_index < len(directions) - 1:
            current_direction_index += 1
        else:
            current_direction_index = 0
            
        
        # Check if done
        if next_map[0][2] == 'Z':
            return num_steps

counts = []
for map in starting_maps:
    counts.append(solve_for_map(map))

print(math.lcm(*counts))