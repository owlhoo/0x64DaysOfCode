import curses
import traceback

try:
    # -- init --
    stdscr = curses.initscr()   # init curses screen
    curses.noecho()             # turn off autoecho of keypresss
    curses.cbreak()             # enter break mode when 'Enter' is pressed
    stdscr.keypad(1)            # enable spec. key values like curses.KEY_LEFT

    # -- Perform an action with scrn --
    stdscr.border(0)
    stdscr.addstr(5, 5, 'Hello, world!', curses.A_BOLD)
    stdscr.addstr(6, 5, 'Press q to close this screen', curses.A_NORMAL)
    i = 6

    while True:
        ch = stdscr.getch()
        i = i + 1
        stdscr.addstr(i, 5, str(ch), curses.A_ITALIC)
        if ch is ord('q'):
            break

    # -- End of user code
except:
    traceback.print_exc()       # print trace back log of the error

finally:
    # -- CLEANUP ON EXIT
    stdscr.keypad(0)
    curses.echo()
    curses.nocbreak()
    curses.endwin()

