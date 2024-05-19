# Use list comprehension to open the file and parse through
day = 13
lines = [line.strip() for line in open("day-" + str(day) + "/data.txt", "r")]

def check_reflect(map: list[str], horizontal: int, vertical: int) -> bool:
    '''Checks if the map can be reflected in that way and still be the same'''
    reflection = [] * len(map)
    
    # Change vertical and horizontal to start at 0 instead of 1
    if horizontal > 0 and vertical > 0:
        raise Exception("Only make horizontal or vertical greater than 0")
    
    if horizontal >= len(map) or vertical >= len(map[0]) or (horizontal == 0 and vertical < 1) or (vertical == 0 and horizontal < 1):
        raise Exception("Index entered does is out of bounds or will not work.")
    
    horizontal -= 1
    vertical -= 1
    
    if horizontal >= 0:
        # Check for allignment
        for i in range(horizontal + 1):
            if horizontal + i + 1 < len(map) and horizontal - i >= 0:
                if map[horizontal + i + 1] != map[horizontal - i]:
                    return False

    if vertical >= 0:
        verticals = [''] * len(map[0])
        
        # Turn into a vertical map
        for j in range(len(map[0])):
            for i, line in enumerate(map):
                verticals[j] += (line[j])

        # Check for allignment
        for i in range(vertical + 1):
            if vertical + i + 1 < len(verticals) and vertical - i >= 0:
                if verticals[vertical + i + 1] != verticals[vertical - i]:
                    return False
    
    return True
        
# Split up into each map
maps = []
current_map = []
for i, line in enumerate(lines):
    
    if line == '':
        maps.append(current_map)
        current_map = []
    else:
        current_map.append(line)

maps.append(current_map)
sum = 0
for current_map in maps:
    map_val = 0
    # Check vertical
    for i in range(1, len(current_map[0])):
        if check_reflect(current_map, 0, i):
            map_val = i
    
    # Check horizontal
    for i in range(1, len(current_map)):
        if check_reflect(current_map, i, 0):
            map_val = i * 100
            
    sum += map_val
    # print(map_val)

print(sum)