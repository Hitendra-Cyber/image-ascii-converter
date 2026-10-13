## PGM to ASCII Converter
This was a project i was working on but this is intermediate product because some work came up so i just left it. My original idea was to convert image to ascii art and i made this to learn the basic concepts. In future i may update this file to maek it image to ascii instead a pgm.

## Requirements

- Python 3.10 or later (adjust if your project uses a different version).
- No external libraries are required for PGM processing.

## Project Structure

image-ascii-converter/
├── src/
│   ├── constants.py
│   ├── mapping_to_single.py
│   ├── mapping_to_multiple_row.py
│   └── mapping_to_row.py
│   ├── ascii_to_text.py
│   └── pgm_reader.py
├── examples/
│   └──  sample.pgm
├── README.md
└── requirements.txt
└── main.py

The exact files may differ depending on your implementation.

## How It Works

- Read the PGM file and extract its header information.
- Retrieve the image width, height, maximum brightness, and pixel values.
- Validate the image data and organize the pixels into rows.
- Map each brightness value to a character from the character ramp.
- Combine the converted rows to generate ASCII art.
- Display the result in the terminal or save it to a text file.

## Usage

Run the application from the project root directory.

## Display ASCII Art

python -m src.main examples/sample.pgm

## Example

Input (sample.pgm)

P2
4 3
255
0 60 128 255
255 128 60 0
0 0 200 255

Output

@#+ 
 +#@
@@:

The exact output depends on the character ramp and brightness-mapping ranges defined in the program.

## Limitations

Supports PGM P2 (ASCII grayscale) images only.

Does not directly support JPG, JPEG, or PNG images.

Output appearance depends on the selected character ramp and terminal font.

Colour information is not preserved because the input format is grayscale.

## Future Improvements

- Add support for additional image formats.
- Improve aspect-ratio correction.
- Add more character-ramp options.
- Include automated tests for parsing and conversion.

## Learning Outcomes

This project provides practical experience with Python functions, file handling, lists and nested lists, exception handling, command-line arguments, and Git version control.
