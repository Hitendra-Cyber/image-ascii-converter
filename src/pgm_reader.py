def pgm_opener(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    ## now removes comments new line
    stripped_line = []
    for string in lines:
        new_string = string.strip()
        if new_string == "" or new_string.startswith("#"):
            continue
        else:
            stripped_line.append(new_string)

    lines = stripped_line
    
    dimensions = lines[1].split()
    width = int(dimensions[0])

    # Extract pixel data (lines 4+, index 3:)
    list_output = []
    for item in lines[3:]:
        list_output.extend([int(x) for x in item.split()])

    return list_output, width


## output of goes to this 
def pgm_opener_prints_2D(flat_list, width) -> list[list[int]]:
    result = []
    for i in range(0,len(flat_list), width):
        new_list = flat_list[i:i + width]
        result.append(new_list)
    return result

