# from src.mapping_to_single import map_brightness_char
from src.mapping_to_row import map_brightness_char_list
from src.constants import character_ramp
user_input = input("Enter brightness values separated by spaces: ")
brightness_list = [int(x) for x in user_input.split()]

print(map_brightness_char_list(list_brightness=brightness_list))