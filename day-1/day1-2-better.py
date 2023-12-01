# Use list comprehension to open the file and parse through
lines = [line.strip() for line in open("day-1/day-1.txt", "r")]
all_nums = []

# convert spelled numbers to a real number
for i, line in enumerate(lines):
    lines[i] = lines[i].replace("one", "o1ne")
    lines[i] = lines[i].replace("two", "t2wo")
    lines[i] = lines[i].replace("three", "t3hree")
    lines[i] = lines[i].replace("four", "f4our")
    lines[i] = lines[i].replace("five", "f5ive")
    lines[i] = lines[i].replace("six", "s6ix")
    lines[i] = lines[i].replace("seven", "s7even")
    lines[i] = lines[i].replace("eight", "e8ight")
    lines[i] = lines[i].replace("nine", "n9ine")
    
    print(lines[i])
                
        
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
    
    print(two_nums)
    append_num = int(two_nums[0] + "" + two_nums[1])
    
    all_nums.append(append_num)
    
    # print(append_num)
    

print(sum(all_nums))