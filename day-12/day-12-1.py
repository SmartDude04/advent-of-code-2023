# Use list comprehension to open the file and parse through
day = 12
lines = [line.strip() for line in open("day-" + str(day) + "/sample.txt", "r")]

def get_combos_for_line(line: str, nums: list[int]) -> int:
    '''Returns the number of combinations possible for this line'''
    
    