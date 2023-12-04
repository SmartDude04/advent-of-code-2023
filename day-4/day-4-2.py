# Use list comprehension to open the file and parse through
old_lines = [line.strip() for line in open("day-4/day-4.txt", "r")]
lines = []
# Array storing the number of cards for each scratchcard
# Parse the file and make into array of format lines[line][win/lose][num_pos]
for i, line in enumerate(old_lines):
    line = [line[line.find(": ") + 2 : line.find(" | ")], line[line.find(" | ") + 3 : ]]
    lines.append(line)
    for j, nums in enumerate(line):
        nums = nums.replace("  ", " ")
        lines[i][j] = nums.split()
        # print(lines[i][j]) 

times_to_run = [1] * len(lines)
# print(times_to_run)

def find_points_for_line(line_num):
    
    line = lines[line_num]
    
    num_wins = 0
    for num in line[1]:
        if num in line[0]:
            num_wins += 1
    
    if num_wins == 0:
        return 0
    
    
    return num_wins

def generate_num_cards(card_line):
    card = lines[card_line]
    
    # See how many points this card gets
    card_points = find_points_for_line(card_line)
    
    # See how many times to go repeat this card
    card_times = times_to_run[card_line]
    
    # Update one point per card per times to run
    for i in range(card_times):
        for j in range(card_points):
            times_to_run[card_line + j + 1] += 1
    
    # print(card_points, card_times)

for i, line in enumerate(lines):
    generate_num_cards(i)

print(sum(times_to_run))
# print(times_to_run)