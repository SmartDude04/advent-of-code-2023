# Use list comprehension to open the file and parse through
lines = [line.strip().split() for line in open("day-6/day-6.txt", "r")]
time_distance_pairs = []
product_ways_to_beat = 1
for i, line in enumerate(lines):
    lines[i] = line[1:]
    
for i, set in enumerate(lines[0]):
    time_distance_pairs.append([lines[0][i], lines[1][i]])

def calculate_distance(holding_time, total_time):
    return holding_time * (total_time - holding_time)

for pair in time_distance_pairs:
    total_time = int(pair[0])
    sum_ways_to_beat = 0
    for i in range(1, total_time):
        if calculate_distance(i, total_time) > int(pair[1]):
            sum_ways_to_beat += 1
        
    product_ways_to_beat *= sum_ways_to_beat

print(product_ways_to_beat)