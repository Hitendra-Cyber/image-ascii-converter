def pgm_opener(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    
    dimensions = lines[1].split()
    width = int(dimensions[0])

    # Extract pixel data (lines 4+, index 3:)
    list_output = []
    for item in lines[3:]:
        list_output.extend([int(x) for x in item.split()])

    return list_output, width

def pgm_opener_prints_2D(flat_list, width):
    result = []
    for i in range(0,len(flat_list), width):
        new_list = flat_list[i:i + width]
        result.append(new_list)
    return result

# def pgm_opener(filename):
#     with open(filename, 'r') as f:
#         lines = f.readlines()
#     print(f"Magic number:{lines[0].strip()}")
#     dimension_line = lines[1].strip()
#     dimension = dimension_line.split()
#     print(f"Width {dimension[0]}, height {dimension[1]}")
#     print(f"Maximum brightness: {lines[2]}")