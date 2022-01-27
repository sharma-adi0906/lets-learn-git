# Some ANSI escape sequences for colours and effects
BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'

BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'


def colour_print(text: str, effect: str) -> None:
    """
    Print `text` using ANSI sequences to change colour,etc

    :param text: the text to print.
    :param effect: the effect we want. one of the constants
        defined at t he start of this module.
    """
    output_string = "{0}{1}{2}".format(effect, text, RESET)
    print(output_string)

colorama.init()
colour_print("Hello, Red", RED)
# test the colour was reset
print("This should be in default terminal colour")
colour_print("Hello, BLUE", BLUE)
colour_print("Hello, BOLD", BOLD)
colour_print("Hello, UNDERLINE", UNDERLINE)
colour_print("Hello, Reverse", REVERSE)
colour_print("Hello, BLACK", BLACK)
colorama.deinit()