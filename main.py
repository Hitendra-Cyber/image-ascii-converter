import os
from src.pgm_reader import pgm_opener, pgm_opener_prints_2D
from src.mapping_to_multiple_row import map_brightness_list_char_list
from src.ascii_to_text import ascii_to_text



current_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_dir, "examples", "test_images.pgm")
output_path = os.path.join(current_dir, "examples", "output_art.txt")

flat_list, width = pgm_opener(image_path)
result_list = pgm_opener_prints_2D(flat_list=flat_list, width=width)


ascii_art_string = map_brightness_list_char_list(result_list)
print(ascii_art_string)
ascii_to_text(ascii_string=ascii_art_string, output_file=output_path)