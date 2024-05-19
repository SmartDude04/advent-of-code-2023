# Use list comprehension to open the file and parse through
lines = [line.strip() for line in open("day-1/day-1.txt", "r")]
all_nums = []

def change_to_num(line, letter_num):
    if letter_num == 0:
        lines[line] = lines[line].replace("one", "1one")
    elif letter_num == 1:
        lines[line] = lines[line].replace("two", "2two")
    elif letter_num == 2:
        lines[line] = lines[line].replace("three", "3three")
    elif letter_num == 3:
        lines[line] = lines[line].replace("four", "4four")
    elif letter_num == 4:
        lines[line] = lines[line].replace("five", "5five")
    elif letter_num == 5:
        lines[line] = lines[line].replace("six", "6six")
    elif letter_num == 6:
        lines[line] = lines[line].replace("seven", "7seven")
    elif letter_num == 7:
        lines[line] = lines[line].replace("eight", "8eight")
    elif letter_num == 8:
        lines[line] = lines[line].replace("nine", "9nine")

# convert spelled numbers to a real number
for i, line in enumerate(lines):
    all_indexes = []
    all_indexes.append(line.find("one"))
    all_indexes.append(line.find("two"))
    all_indexes.append(line.find("three"))
    all_indexes.append(line.find("four"))
    all_indexes.append(line.find("five"))
    all_indexes.append(line.find("six"))
    all_indexes.append(line.find("seven"))
    all_indexes.append(line.find("eight"))
    all_indexes.append(line.find("nine"))
    
    for k in range(len(line)):
        for j, num in enumerate(all_indexes):
            if num == k:
                change_to_num(i, j)

    # print(all_indexes)
    # print(lines[i])
            
            
        
for line in lines:
    two_nums = []
    # Go forwards into the list and get the first character
    for char in range(len(line)):
        if line[char].isdigit():
            digit = line[char]
            digit = digit
            two_nums.append(digit)
            break
        
    # Go backwards and add that to the twoNums list
    for char in reversed(range(len(line))):
        if line[char].isdigit():
            digit = line[char]
            digit = digit
            two_nums.append(digit)
            break
        
    append_num = int(two_nums[0] + "" + two_nums[1])
    
    all_nums.append(append_num)
    
    # print(append_num)
    

print(sum(all_nums))