from src.mapping_to_row import map_brightness_char_list

def map_brightness_list_char_list(matrix: list[list[int]]) -> str:
    result = []
    for row in matrix:
        result.append(map_brightness_char_list(row))
    return "\n".join(result)