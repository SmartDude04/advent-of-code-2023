# Use list comprehension to open the file and parse through
lines = [line.strip() for line in open("day-5/day-5-snippet.txt", "r")]

seeds = lines[0].split(": ")[1].split()
seeds = [int(seed) for seed in seeds]
lines = lines[3:]
# Remove blank lines
lines = [lines.pop(i) for i in reversed(range(len(lines))) if lines[i] != ""]
lines = lines[::-1]

seed_to_soil = []
soil_to_fertilizer = []
fertilizer_to_water = []
water_to_light = []
light_to_temperature = []
temperature_to_humidity = []
humidity_to_location = []

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
def get_loc_for_seed(seed_num):
    value = seed_num
    value = calculate_destination(seed_to_soil, value)
    value = calculate_destination(soil_to_fertilizer, value)
    value = calculate_destination(fertilizer_to_water, value)
    value = calculate_destination(water_to_light, value)
    value = calculate_destination(light_to_temperature, value)
    value = calculate_destination(temperature_to_humidity, value)
    value = calculate_destination(humidity_to_location, value)
    
    return value

# Get the min location for all the seeds
min_loc = -1
for seed in seeds:
    seed_loc = get_loc_for_seed(seed)
    if seed_loc < min_loc or min_loc == -1:
        min_loc = seed_loc
        
print(min_loc)