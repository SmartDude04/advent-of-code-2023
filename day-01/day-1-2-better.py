# Use list comprehension to open the file and parse through
lines = [line.strip() for line in open("day-1/day-1.txt", "r")]
all_nums = []

# convert spelled numbers to a real number
for i, line in enumerate(lines):
    line = line.replace("one", "o1ne")
    line = line.replace("two", "t2wo")
    line = line.replace("three", "t3hree")
    line = line.replace("four", "f4our")
    line = line.replace("five", "f5ive")
    line = line.replace("six", "s6ix")
    line = line.replace("seven", "s7even")
    line = line.replace("eight", "e8ight")
    line = line.replace("nine", "n9ine")

    lines[i] = line    
    # print(line)
    
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
    
    # print(two_nums)
    append_num = int(two_nums[0] + "" + two_nums[1])
    
    all_nums.append(append_num)
    
    # print(append_num)
    

print(sum(all_nums))