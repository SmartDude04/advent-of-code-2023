# Use list comprehension to open the file and parse through
lines = [line.strip() for line in open("day-5/day-5-snippet.txt", "r")]

seeds = lines[0].split(": ")[1].split()

lines = lines[3:]

print(lines)
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
            seed_to_soil.append(line)
        elif current_map == 2:
            seed_to_soil.append(line)
        elif current_map == 3:
            seed_to_soil.append(line)
        elif current_map == 4:
            seed_to_soil.append(line)
        elif current_map == 5:
            seed_to_soil.append(line)
        elif current_map == 6:
            seed_to_soil.append(line)
    
print(seed_to_soil)