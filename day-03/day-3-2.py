# Use list comprehension to open the file and parse through
old_lines = [line.strip() for line in open("day-3/day-3.txt", "r")]
lines = []

# Make lines into 2D array
# This will have two coordanites
for i, line in enumerate(old_lines):
    
    lines.append([])
    
    for j, char in enumerate(line):
        lines[i].append(char)

def find_num(x, y):
    go_backwards = False
    both_directions = False
    line = lines[y]
    if line[x - 1] in {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}:
        go_backwards = True
        if line[x + 1] in {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}:
            both_directions = True
        
    
    num = line[x]
    
    if not go_backwards:
        for i in range(x + 1, len(line)):
            if line[i] in {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}:
                num += line[i]
            else:
                break
    else:
        for i in reversed(range(0, x)):
            if line[i] in {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}:
                num += line[i]
            else:
                break
        num = num[::-1]
    
    if both_directions:
        for i in range(x + 1, len(line)):
            if line[i] in {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}:
                num += line[i]
            else:
                break
    
    return num

def find_if_works(x_coord, y_coord):
    
    number = ''
    
    # Find possible coordanites for characters around the number
    possible_coords = []
    for y in range(y_coord - 1, y_coord + 2):
        for x in range(x_coord - 1, x_coord + 2):
            if x >= 0 and y >= 0 and x < len(lines[0]) and y < len(lines):
                possible_coords += lines[y][x]
    
    
    # Split up possible_coords into three vertical slices where to check for a number
    possible_coords = [[possible_coords[0], possible_coords[1], possible_coords[2]],
                       [possible_coords[3],possible_coords[4], possible_coords[5]],
                       [possible_coords[6], possible_coords[7], possible_coords[8]]]
    
    
    num_nums = 0
    product_of_nums = 1
    
    top_nums = []
    
    # Check for numbers on the top slice
    if possible_coords[0][0] in {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}:
        top_nums.append(find_num(x_coord - 1, y_coord - 1))
    if possible_coords[0][1] in {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}:
        top_nums.append(find_num(x_coord, y_coord - 1))
    if possible_coords[0][2] in {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}:
        top_nums.append(find_num(x_coord + 1, y_coord - 1))
    
    # Check to see if any are the same, if so then there is one number on the top
    if (len(top_nums) == 2 or len(top_nums) == 3) and len(set(top_nums)) == 1:
        product_of_nums *= int(top_nums[0])
        num_nums += 1
    elif len(top_nums) == 2:
        product_of_nums *= int(top_nums[0]) * int(top_nums[1])
        num_nums += 2
    elif len(top_nums) == 1:
        product_of_nums *= int(top_nums[0])
        num_nums += 1
        
    middle_nums = []
    
    # Check the numbers in the middle
    if possible_coords[1][0] in {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}:
        middle_nums.append(find_num(x_coord - 1, y_coord))
    if possible_coords[1][2] in {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}:
        middle_nums.append(find_num(x_coord + 1, y_coord))
    
    if len(middle_nums) == 1:
        product_of_nums *= int(middle_nums[0])
        num_nums += 1
    elif len(middle_nums) == 2:
        product_of_nums *= int(middle_nums[0]) * int(middle_nums[1])
        num_nums += 2
    
    bottom_nums = []
    
    # Check the numbers on the bottom
    if possible_coords[2][0] in {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}:
        bottom_nums.append(find_num(x_coord - 1, y_coord + 1))
    if possible_coords[2][1] in {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}:
        bottom_nums.append(find_num(x_coord, y_coord + 1))
    if possible_coords[2][2] in {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}:
        bottom_nums.append(find_num(x_coord + 1, y_coord + 1))
       
    
    if (len(bottom_nums) == 2 or len(bottom_nums) == 3) and len(set(bottom_nums)) == 1:
        product_of_nums *= int(bottom_nums[0])
        num_nums += 1
    elif len(bottom_nums) == 2:
        product_of_nums *= int(bottom_nums[0]) * int(bottom_nums[1])
        num_nums += 2
    elif len(bottom_nums) == 1:
        product_of_nums *= int(bottom_nums[0])
        num_nums += 1
    
    
        
    if num_nums != 2:
        return 0
    else:
        return product_of_nums
            

# Go through and try all *'s
sum_of_products = 0
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == '*':
            # print(x, y, find_if_works(x, y), char)
            sum_of_products += find_if_works(x, y)

print(sum_of_products)