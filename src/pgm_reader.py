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
    # CHANGE 1: Flatten all elements after the P2 header to safely handle multi-line metadata
    all_tokens = []
    for string in lines:
        all_tokens.extend(string.split())

    # CHANGE 2: Extract variables sequentially from the token list instead of hardcoded line indexes
    width = int(all_tokens[0])
    height = int(all_tokens[1])

    if width == 0 or width < 0 or height == 0 or height < 0:
        raise ValueError

    brightness = int(all_tokens[2])

    if brightness < 0:
        raise ValueError
    
    # Extract pixel data (everything after index 2)
    list_output = []
    # CHANGE 3: Iterate through tokens starting strictly from index 3 onwards
    for x in all_tokens[3:]:
        if int(x) < 0 or int(x) > brightness:
            raise ValueError
        else:
            list_output.extend([int(x)])

    # CHANGE 4: Fixed comparison syntax to check for strict equality 
    if len(list_output) != (width*height):
        raise Exception("No. of pixels defined in file in total are not strictly equal to dimension")
    
    return list_output, width


## output of goes to this 
def pgm_opener_prints_2D(flat_list, width) -> list[list[int]]:
    result = []
    for i in range(0,len(flat_list), width):
        new_list = flat_list[i:i + width]
        result.append(new_list)
    return result
