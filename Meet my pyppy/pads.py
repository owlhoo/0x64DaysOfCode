import curses as c


def main():
    try:
        stdscr = c.initscr()
        c.nocbreak()
        c.noecho()
        stdscr.keypad(1)

        c.start_color()
        stdscr.clear()
        pad = c.newpad(100, 100)
        # fill out whole pad with stuff
        for y in range(0, 99):
            for x in range(0, 99):
                pad.addch(y, x, ord('a') + (x * x + y * y) % 26, c.A_REVERSE)

        # hide the cursor
        c.curs_set(True)
        pad.addstr(0, 0, 'HELLO WORLD', c.A_BLINK)
        pad.addstr(5, 5, 'IM IN COLOR MODE', c.color_pair(1))

        pad.refresh(0, 0, 5, 5, 20, 75)
        pad.getkey()
    finally:
        stdscr.keypad(0)
        c.echo()
        c.cbreak()
        c.endwin()

main()


# c.wrapper(main)
