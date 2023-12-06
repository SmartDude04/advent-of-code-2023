# Use list comprehension to open the file and parse through
lines = [line.strip() for line in open("day-5/day-5-snippet.txt", "r")]

seed_pairs = lines[0].split(": ")[1]
pos_num = 0


# Update seeds for part 2
seeds = []


lines = lines[3:]
# Remove blank lines
lines = [lines.pop(i) for i in reversed(range(len(lines))) if lines[i] != ""]
lines = lines[::-1]

# SOLUTION TO FIX SLOW CODE:
# 
# If we already know where a specific mapping
# leads to, we don't have to run it again. So, at each point check if the mapping
# was run before and return false if so. This will indicate to move on to the 
# Next number

seeds_complete = []

seed_to_soil = []
seed_to_soil_complete = []

soil_to_fertilizer = []
soil_to_fertilizer_complete = []

fertilizer_to_water = []
fertilizer_to_water_complete = []

water_to_light = []
water_to_light_complete = []

light_to_temperature = []
light_to_temperature_complete = []

temperature_to_humidity = []
temperature_to_humidity_complete = []

humidity_to_location = []
humidity_to_location_complete = []

current_map = 0
for line in lines:
    if not line[0].isdigit():
        current_map += 1
    else:
        if current_map == 0:
            seed_to_soil.append(line)
        elif current_map == 1:
            soil_to_fertilizer.append(line)
        elif current_map == 2:
            fertilizer_to_water.append(line)
        elif current_map == 3:
            water_to_light.append(line)
        elif current_map == 4:
            light_to_temperature.append(line)
        elif current_map == 5:
            temperature_to_humidity.append(line)
        elif current_map == 6:
            humidity_to_location.append(line)
    
# Based on map data passed in, calculate the destination number for a starting source number
def calculate_destination(map, source):
    
    for part in map:
        map_piece = part.split()
        map_piece = [int(num) for num in map_piece]
        if source >= map_piece[1] and source <= (map_piece[1] + map_piece[2] - 1):
            return int(map_piece[0]) + (source - int(map_piece[1]))
    
    return source

# Go through a seed number and get a location for it
# NEW: Return False if the number was done already
def get_loc_for_seed(seed_num):
    
    value = seed_num
    if value in seeds_complete:
        return False
    else:
        seeds_complete.append(value)
        
    value = calculate_destination(seed_to_soil, value)
    if value in seed_to_soil_complete:
        return False
    else:
        seed_to_soil_complete.append(value)
        
    value = calculate_destination(soil_to_fertilizer, value)
    if value in soil_to_fertilizer_complete:
        return False
    else:
        soil_to_fertilizer_complete.append(value)
        
    value = calculate_destination(fertilizer_to_water, value)
    if value in fertilizer_to_water_complete:
        return False
    else:
        fertilizer_to_water_complete.append(value)
    
    value = calculate_destination(water_to_light, value)
    if value in water_to_light_complete:
        return False
    else:
        water_to_light_complete.append(value)
    
    value = calculate_destination(light_to_temperature, value)
    if value in light_to_temperature_complete:
        return False
    else:
        light_to_temperature_complete.append(value)
        
    value = calculate_destination(temperature_to_humidity, value)
    if value in temperature_to_humidity_complete:
        return False
    else:
        temperature_to_humidity_complete.append(value)
        
    value = calculate_destination(humidity_to_location, value)
    if value in humidity_to_location_complete:
        return False
    else:
        humidity_to_location_complete.append(value)
    
    return value

# Get the min location for all the seeds
min_loc = -1
for seed in seeds:
    seed_loc = get_loc_for_seed(seed)
    if seed_loc == False:
        continue
    elif seed_loc < min_loc or min_loc == -1:
        min_loc = seed_loc
        
print(min_loc)