import curses


def main(stdscr):
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_WHITE)  # init pair
    stdscr.addstr("Pretty text", curses.color_pair(1))
    stdscr.refresh()
    stdscr.getkey()


curses.wrapper(main)
