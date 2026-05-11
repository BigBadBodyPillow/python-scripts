import re
import sys

x = 100
y = 100


def adjust_coordinates_raw(input_file, output_file):
    with open(input_file, "r", encoding="utf-8-sig") as f:
        text = f.read()

    # Add 100 to all x values
    text = re.sub(r'"x":\s*(\d+)', 
                  lambda m: f'"x": {int(m.group(1)) + x}', 
                  text)

    # Add 100 to all y values
    text = re.sub(r'"y":\s*(\d+)', 
                  lambda m: f'"y": {int(m.group(1)) + y}', 
                  text)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(text)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python test.py <input.hideout> <output.hideout>")
    else:
        adjust_coordinates_raw(sys.argv[1], sys.argv[2])


# python decoration_offset.py <input.hideout> <output.hideout>