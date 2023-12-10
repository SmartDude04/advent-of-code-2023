# Use list comprehension to open the file and parse through
lines = [line.strip() for line in open("day-2/day-2.txt", "r")]

# Declare constants
MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

# returns the max points for that round
def find_max(round_marbles, round_colors):
    
    # Change round_marbles to int's
    for i, game in enumerate(round_marbles):
        for j, point in enumerate(game):
            round_marbles[i][j] = int(point)
    
    top_red = 0
    top_green = 0
    top_blue = 0
    
    # Go through and update each point as needed
    for i in range(len(round_marbles)):
        for j in range(len(round_marbles[i])):
            color = round_colors[i][j]
            points = round_marbles[i][j]
            
            if color == 'r':
                if points > top_red:
                    top_red = points
            elif color == 'g':
                if points > top_green:
                    top_green = points
            elif color == 'b':
                if points > top_blue:
                    top_blue = points
                    
    max = top_red * top_green * top_blue
    return max

# Returns the game value if it works or 0 if it doesn't
def get_power(index):
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
        
    return find_max(round_marbles, round_colors)
    
    
# Use the functions to add up all the points from each line
sum_rounds_that_work = 0
for i, line in enumerate(lines):
    sum_rounds_that_work += get_power(i)


print(sum_rounds_that_work)