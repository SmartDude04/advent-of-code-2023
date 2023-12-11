# Use list comprehension to open the file and parse through
lines = [line.strip() for line in open("day-10/day-10.txt", "r")]

def sign(number: int) -> int:
    '''Returns 1 if the number is positive, -1 if negative, and 0 if 0'''
    if number > 0:
        return 1
    elif number < 0:
        return -1
    else:
        return 0

def calculate_next_coord(current_coords:list[int], destination_coords:list[int]) -> list[int]:
    '''Sees which distance to the coordanite is longer and decides to go that way.
    This will return the value that will lead to the shortest path to the next galaxy'''
    
    distance_in_x = destination_coords[0] - current_coords[0]
    distance_in_y = destination_coords[1] - current_coords[1]
    
    if abs(distance_in_x) > abs(distance_in_y):
        return [current_coords[0] + sign(distance_in_x), current_coords[1]]
    else:
        return [current_coords[0], current_coords[1] + sign(distance_in_y)]

def input_extra_row(array: list[str], row_num: int) -> None:
    '''Will add an extra row below the specified row'''
    
    extra_row = ['.'*len(array)]
    
    array.insert(row_num, extra_row)
    