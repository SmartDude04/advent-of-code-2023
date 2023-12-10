# Use list comprehension to open the file and parse through
old_lines = [line.strip() for line in open("day-4/day-4-snippet.txt", "r")]
lines = []
# Parse the file and make into array of format lines[line][win/lose][num_pos]
for i, line in enumerate(old_lines):
    line = [line[line.find(": ") + 2 : line.find(" | ")], line[line.find(" | ") + 3 : ]]
    lines.append(line)
    for j, nums in enumerate(line):
        nums = nums.replace("  ", " ")
        lines[i][j] = nums.split()
        # print(lines[i][j])
    


def find_points_for_line(line_num):
    
    line = lines[line_num]
    
    num_wins = 0
    for num in line[1]:
        if num in line[0]:
            num_wins += 1
    
    if num_wins == 0:
        return 0
    
    num_wins = 2 ** (num_wins - 1)
    
    return num_wins

sum = 0
for i, line in  enumerate(lines):
    sum += find_points_for_line(i)
    
print(sum)
