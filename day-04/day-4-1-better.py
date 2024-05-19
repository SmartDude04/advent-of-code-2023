# Use list comprehension to open the file and parse through
lines = [line.strip() for line in open("day-4/day-4.txt", "r")]

total = 0

for line in lines:
    groups = line.split(":")[1].split("|")
    winning_nums = [num.strip() for num in groups[0].split()]
    person_nums = [num.strip() for num in groups[1].split()]
    count = 0
    
    for win in winning_nums:
        if win in person_nums:
            count += 1
    
    if count > 0:
        total += 2 ** (count - 1)
            
    print(count)

print(total)