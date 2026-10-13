

def ascii_to_text(ascii_string, output_file):
    with open(f"{output_file}", "w", newline="") as f:
        f.write(ascii_string)