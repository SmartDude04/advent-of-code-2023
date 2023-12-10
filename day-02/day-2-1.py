# Use list comprehension to open the file and parse through
lines = [line.strip() for line in open("day-2/day-2.txt", "r")]

# Declare constants
MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

# Returns true if it works, false if it doesn't
def test(marble, color):
    marble = int(marble)
    if color == 'r':
        if marble <= MAX_RED:
            return True
        else:
            return False
    elif color == 'g':
        if marble <= MAX_GREEN:
            return True
        else:
            return False
    elif color == 'b': # Could be an else but I prefer to be safer
        if marble <= MAX_BLUE:
            return True
        else:
            return False
    
# Returns the game value if it works or 0 if it doesn't
def find_if_works(index):
    line = lines[index]
    # This is an array of arrays. Each inner array stores three values, coresponsing to
    # red, green, and blue marbles respectively
    round_marbles = []
    # This has the same format as round_marbles but stores the color corresponding to the
    # marble count. Stored as a string of r, g, or b
    round_colors = []
    
    # Get the game number
    game_num = index + 1
    
    # remove extra text from the line
    remove = line.find(":") + 2
    line = line[remove:]
    
    # Split the string up into parts for each game then parts for each marble
    line = line.split("; ")
    
    for i, game in enumerate(line):
        line[i] = game.split(", ")
    
    # Get an array of colors the correspond to the marbles array
    for i, game in enumerate(line):
        
        colors_for_round = []
        
        for j, marble in enumerate(game):
            remove = marble.find(" ")
            marble = marble[remove + 1:remove + 2]
            colors_for_round.append(marble)
        
        round_colors.append(colors_for_round)
    
    
    # Finish adding the marble count to the round_marbles array
    for i, game in enumerate(line):
        
        points_for_round = []
        
        for j, count in enumerate(game):
            remove = count.find(" ")
            count = count[:remove]
            
            points_for_round.append(count)
        
        round_marbles.append(points_for_round)
    
    
    # print(round_marbles)
    # print(round_colors)
    
    # Now that we have completed arrays, pass each value pair into a function to find if one is too high
    # If none are too high, return the value of the game
    for i, game in enumerate(round_marbles):
        for j, part in enumerate(game):
            marble = round_marbles[i][j]
            color = round_colors[i][j]
            
            if not test(marble, color):
                return 0
            
    return game_num
            
            
    
# Use the functions to add up all the points from each line
sum_rounds_that_work = 0
for i, line in enumerate(lines):
    sum_rounds_that_work += find_if_works(i)


print(sum_rounds_that_work)