def pgm_opener(filename):
    list_output = []
    with open(filename, 'r') as f:
        lines = f.readlines()[3:]
    for item in lines:
        list_output.extend([int(x) for x in item.split()])

    print(list_output) 