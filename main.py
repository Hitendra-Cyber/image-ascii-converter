import os
from src.pgm_reader import pgm_opener

current_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_dir, "examples", "samples.pgm") 

pgm_opener(image_path)