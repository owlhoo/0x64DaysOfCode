import curses

from time import sleep


def main(stdscr):
    # clear screen
    stdscr.clear()

    # This raises ZeroDivisionError when i == 10
    stdscr.addstr(0, 0, 'Enter something:')
    for i in range(0, 10):
        v = i - 10
        key = stdscr.getkey()
        stdscr.addstr(0, 0, f'     ')
        stdscr.addstr(i, 5, f'10 divided by {v} is {10/v}, btw you pressed {key}')
        sleep(.2)
        stdscr.refresh()

    begin_x = 250
    begin_y = 75
    height = 2
    width = 1
    win = curses.newwin(height, width, begin_y, begin_x)

    stdscr.clear()
    
    stdscr.addstr(0, 0, 'I am a new screen')

    stdscr.getkey()


curses.wrapper(main)
