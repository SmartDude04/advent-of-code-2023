# Use list comprehension to open the file and parse through
lines = [line.strip() for line in open("day-5/day-5.txt", "r")]

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

# Perform a reverse lookup for destination --> seed
# Returns false if no seed present
def reverse_calculate_destination(map, destination):
    
    for part in map:
        map_piece = part.split()
        map_piece = [int(num) for num in map_piece]
        if destination >= map_piece[0] and destination <= (map_piece[0] + map_piece[2] - 1):
            return int(map_piece[1]) + (destination - int(map_piece[0]))
    
    return destination

# Go through a seed number and get a location for it
def get_seed_for_loc(loc_num):
    value = loc_num
    value = reverse_calculate_destination(humidity_to_location, value)
    value = reverse_calculate_destination(temperature_to_humidity, value)
    value = reverse_calculate_destination(light_to_temperature, value)
    value = reverse_calculate_destination(water_to_light, value)
    value = reverse_calculate_destination(fertilizer_to_water, value)
    value = reverse_calculate_destination(soil_to_fertilizer, value)
    value = reverse_calculate_destination(seed_to_soil, value)
    
    return value
    
def check_if_seed(seed):
    for i in range(0, len(seeds), 2):
        if seed >= seeds[i] and seed < (seeds[i] + seeds[i + 1] - 1):
            return True
    
    return False
    
# Go through the locations and see if it matches to a seed
check_loc = 1
while True:
    if check_loc % 100000 == 0:
        print("Checking location " + str(check_loc) + "...")
        
    seed_val = get_seed_for_loc(check_loc)
    
    if check_if_seed(seed_val):                
            print(check_loc)
            break
    
    check_loc += 1
