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
    red = get_value(prompt="Enter a Red value:\t", lower=0-1, upper=255+1, convert_type=int)
    green = get_value(prompt="Enter a Green value:\t", lower=0-1, upper=255+1, convert_type=int)
    blue = get_value(prompt="Enter a Blue value:\t", lower=0-1, upper=255+1, convert_type=int)
    rgb_values = {
        "red": red,
        "green": green,
        "blue": blue,
    }
    display_table(rgb_values)

if __name__ == "__main__":
    main()
