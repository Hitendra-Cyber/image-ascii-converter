def pgm_opener(filename):
    with open(filename, 'r') as f:
        first_line = f.readline()
        if not first_line.startswith("P2"):
            raise Exception("The file header doesn't starts with P2")
        lines = f.readlines()

    # now removes comments new line
    stripped_line = []
    for string in lines:
        new_string = string.strip()
        if new_string == "" or new_string.startswith("#"):
            continue
        else:
            stripped_line.append(new_string)

    lines = stripped_line

    # handling edge cases 
    
    
    dimensions = lines[1].split()
    width = int(dimensions[0])
    height = int(dimensions[1])

    if width == 0 or width < 0 or height == 0 or height < 0:
        raise ValueError

    brightness = int(dimensions[2])

    if brightness < 0:
        raise ValueError
    
    
    # Extract pixel data (lines 4+, index 3:)
    list_output = []
    for item in lines[3:]:
        for x in item.split():
            if int(x) < 0 or int(x) > brightness:
                raise ValueError
            else:
                list_output.extend([int(x)])

    if width*height > len(list_output) < width*height:
        raise Exception("No. of pixels defined in file in total are not strictly equal to dimension")
    
    return list_output, width


## output of goes to this 
def pgm_opener_prints_2D(flat_list, width) -> list[list[int]]:
    result = []
    for i in range(0,len(flat_list), width):
        new_list = flat_list[i:i + width]
        result.append(new_list)
    return result

