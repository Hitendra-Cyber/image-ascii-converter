# from src.mapping_to_single import map_brightness_char
# from src.mapping_to_row import map_brightness_char_list
from src.mapping_to_multiple_row import map_brightness_list_char_list
from src.constants import character_ramp
matrix = []

print("Enter brightness values separated by spaces (Press ENTER on an empty line to finish):")

while True:
    user_input = input().strip()
    # Check if the user pressed Enter without typing anything
    if not user_input: 
        break 
    brightness_list = [int(x) for x in user_input.split()]
    matrix.append(brightness_list)

if matrix:
    ascii_art = map_brightness_list_char_list(matrix)
    print(ascii_art)
else:
    print("No input provided.")