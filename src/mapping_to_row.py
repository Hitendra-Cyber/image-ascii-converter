from src.mapping_to_single import map_brightness_char

def map_brightness_char_list(list_brightness: list[int]) -> str:
    result = ""
    for value in list_brightness:
        result += map_brightness_char(value)
    return result