import curses

try:
    stdscr = curses.initscr()

    # no echo xd
    curses.noecho()

    # read key without enter
    curses.cbreak()

    # multibyte escape sequences like curses.KEY_LEFT
    stdscr.keypad(True)

    stdscr.addstr(0, 0, 'Enter q to quit', curses.A_ITALIC)

    while True:
        q = stdscr.getch()
        if q is ord('q'):
            break

    # ending the app
finally:
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()

# wrapper from curses does this by default xd