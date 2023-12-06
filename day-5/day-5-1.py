# Use list comprehension to open the file and parse through
lines = [line.strip() for line in open("day-5/day-5-snippet.txt", "r")]

# Get values for each part
all_maps = [[], [], [], [], [], [], []]

seeds = lines[0]
seeds = seeds[7:].split()
lines = lines[2:]

lines = [lines.pop(i) for i in reversed(range(len(lines))) if lines[i] != ""]
lines = [line.split() for line in lines]
lines = lines[::-1]

current_map_index = 0
for i, line in enumerate(lines):
    # If the element is not a digit, we know it is the start of a new section
    
    if line[1] == 'map:':
        do_break = False
        for row in lines[i + 1:]:
            if row[0].isdigit():
                all_maps[current_map_index].append(row)
            else:
                current_map_index += 1
                break

# Generate full maps
for i, map in enumerate(all_maps):
    full_map = [i for i in range(100)]
    print(full_map)
    for j, gen_map in enumerate(map):
        iterations = gen_map[2]
        start = gen_map[0]
        source = gen_map[1]
        
        

# # Find the lowest seed
# def get_location_for_seed(seed_index):
#     seed = seeds[seed_index]
    
#     current_spot = seed
#     for map in all_maps:
        

print(all_maps)