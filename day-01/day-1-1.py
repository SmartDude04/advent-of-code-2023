# Use list comprehension to open the file and parse through
lines = [line.strip() for line in open("day-1/day-1.txt", "r")]
all_nums = []
    
for line in lines:
    two_nums = []
    # Go forwards into the list and get the first character
    for char in range(len(line)):
        if line[char].isdigit():
            digit = line[char]
            two_nums.append(digit)
            break
        
    # Go backwards and add that to the twoNums list
    for char in reversed(range(len(line))):
        if line[char].isdigit():
            digit = line[char]
            two_nums.append(digit)
            break
        
    append_num = int(two_nums[0] + "" + two_nums[1])
    
    all_nums.append(append_num)
    

print(sum(all_nums))