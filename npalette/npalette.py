#!/usr/bin/env python3

from .utils.get_value import get_value

# Helper functions
def print_splash():
    splash = r"""

             
        ███╗   ██╗██████╗  █████╗ ██╗     ███████╗████████╗████████╗███████╗
        ████╗  ██║██╔══██╗██╔══██╗██║     ██╔════╝╚══██╔══╝╚══██╔══╝██╔════╝
        ██╔██╗ ██║██████╔╝███████║██║     █████╗     ██║      ██║   █████╗  
        ██║╚██╗██║██╔═══╝ ██╔══██║██║     ██╔══╝     ██║      ██║   ██╔══╝  
        ██║ ╚████║██║     ██║  ██║███████╗███████╗   ██║      ██║   ███████╗
        ╚═╝  ╚═══╝╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝   ╚═╝      ╚═╝   ╚══════╝
              
                                    NPalette
                           A Terminal RGB Swatch Tool
                                                                    
"""
    print(splash)

def print_border(char="=", width=80):
    print(char * width)

def print_header(title, width=80):
    print_border()
    for line in title.split("\n"):
        print(f"{line.center(width)}")
    print_border()

def print_author(title, width=80):
    print_border()
    print(f"{title.center(width)}")
    print_border()

# Define program resources
resources = {
    "HEADER_1": "Welcome to the NPalette RGB Swatch Tool\nNPalette",
    "HEADER_2": "Select RGB Values for a CLI Swatch Display",
    "AUTHOR": "Pavle Džakula, 2025, GPLv3",
}

def rgb_to_hex(r: int, g: int, b: int) -> str:
    return f"#{r:02X}{g:02X}{b:02X}"

def display_table(rgb_values):
    color_width = 25
    swatch_width = 8 
    hex_width = 15

    print(f"{'Color (RGB)':<{color_width}}{'Swatch':<{swatch_width}}{'HTML/CSS':>{hex_width}}")
    print("-" * (color_width + swatch_width + hex_width))

    r, g, b = rgb_values['red'], rgb_values['green'], rgb_values['blue']
    color = f"R:{r}, G:{g}, B:{b}"
    hex_value = rgb_to_hex(r, g, b)
    swatch = f"\033[38;2;{r};{g};{b}m▣\033[0m{' ' * (swatch_width - 1)}"
    print(f"{color:<{color_width}}{swatch:<{swatch_width}}{hex_value:>{hex_width}}")

def show_headers():
    print_splash()
    print_header(resources["HEADER_1"])
    print_header(resources["HEADER_2"])
    print_author(resources["AUTHOR"])
    print_border()

def main():
    show_headers()
    while True:
        def read_channel(name: str) -> int:
            while True:
                raw = get_value(
                    prompt=f"Enter a {name} value (0–255) or 'q' to quit:\t").strip().lower()
                if raw == "q":
                    print("Goodbye!")
                    raise SystemExit
                try:
                    val = int(raw)
                except ValueError:
                    print("Error: please enter an integer (0–255) or 'q' to quit.")
                    continue
                if 0 <= val <= 255:
                    return val
                else:
                    print("Out of range: expected 0–255.")
        r = read_channel("Red")
        g = read_channel("Green")
        b = read_channel("Blue")
        rgb_values = {"red": r, "green": g, "blue": b}
        display_table(rgb_values)
        again = get_value(
            prompt="Press Enter for another swatch, or type 'q' to quit:\t",
            convert_type=str
        ).strip().lower()
        if again == "q":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
