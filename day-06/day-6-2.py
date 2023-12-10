# Use list comprehension to open the file and parse through
lines = [line.strip() for line in open("day-6/day-6.txt", "r")]
time_distance_pair = []
product_ways_to_beat = 1
for i, line in enumerate(lines):
    line = line.replace(' ', '')
    lines[i] = line.split(":")[1]
# print(lines)

time_distance_pair = lines

def calculate_distance(holding_time, total_time):
    return holding_time * (total_time - holding_time)


total_time = int(time_distance_pair[0])
sum_ways_to_beat = 0
for i in range(1, total_time):
    if calculate_distance(i, total_time) > int(time_distance_pair[1]):
        sum_ways_to_beat += 1
    
product_ways_to_beat *= sum_ways_to_beat

print(product_ways_to_beat)