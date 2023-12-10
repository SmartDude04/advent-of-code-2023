# Use list comprehension to open the file and parse through
old_lines = [line.strip().split() for line in open("day-9/day-9.txt", "r")]
lines = []

# Change all values to ints
for i, line in enumerate(old_lines):
    new_line = []
    for j, val in enumerate(line):
        new_line.append(int(val))
    lines.append(new_line)


def calc_derivs(pattern_array):
    set_of_derivs = [pattern_array]
    
    
    while True:
        last_deriv = set_of_derivs[-1]
        current_deriv = []
        
        for i in range(1, len(last_deriv)):
            current_deriv.append(last_deriv[i] - last_deriv[i - 1])
        
        set_of_derivs.append(current_deriv)
                
        # Check if the set is all 0
        deriv_set = set(current_deriv)
        if len(deriv_set) == 1 and 0 in deriv_set:
            break
    
    return set_of_derivs

def get_next_value(derivs_set) -> int:
    
    derivs = derivs_set
    for i in reversed(range(len(derivs_set) - 1)):
        
        derivs[i].append(derivs_set[i + 1][-1] + derivs_set[i][-1])
        
    return derivs[0][-1]
        
    
         
sum_next_values = 0
for line in lines:
    sum_next_values += get_next_value(calc_derivs(line))
    
print(sum_next_values)