import curses
from aicli100.cli import input_bar, initialize_screen

def main(stdscr: curses.window):
    initialize_screen(stdscr)
    input_received = input_bar()
    while input_received != "/exit":
        input_received = input_bar()
    


if __name__ == "__main__":
    curses.wrapper(main)