import curses
from aicli100.cli import input_bar, initialize_screen
from aicli100.setup import create_config_file


def main(stdscr=None):
    if stdscr is None:
        return curses.wrapper(main)

    create_config_file()
    initialize_screen(stdscr)
    input_received = input_bar()
    while input_received != "/exit":
        input_received = input_bar()
    


if __name__ == "__main__":
    curses.wrapper(main)