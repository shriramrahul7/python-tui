import random
import requests
import json
import curses as c
import time

stdscr = c.initscr()

# Initialising Colors

def getQuotes():
    response = requests.get('https://type.fit/api.quotes')
    jsondata = json.loads(response.text)
    quote = random.choice(jsondata)
    quoteStr = quote['text'] + '\n   - ' + quote['author'] 

def main(stdscr):
    c.curs_set(0)
    c.init_pair(1, c.COLOR_RED, c.COLOR_BLACK)
    c.init_pair(2, c.COLOR_GREEN, c.COLOR_BLACK)
    c.init_pair(3, c.COLOR_BLUE, c.COLOR_BLACK)

    stdscr.addstr(' RANDOM QUOTES GENERATOR', c.A_REVERSE)
    stdscr.chgat(-1, c.A_REVERSE)

    stdscr.addstr(c.LINES-1, 0, 'Press "R" for next quote or "Q" to exit')
    stdscr.chgat(c.LINES-1, 7, 1, c.A_BOLD | c.color_pair(2))
    stdscr.chgat(c.LINES-1, 29, 1, c.A_BOLD | c.color_pair(1))

    quote_window = c.newwin(c.LINES-2, c.COLS, 1, 0)
    quote_text_window = quote_window.subwin(c.LINES-6, c.COLS-4, 3, 2)

    quote_text_window.addstr("Press 'R' to generate a new quote.")
    quote_window.box()

    stdscr.noutrefresh()
    quote_window.noutrefresh()
    c.doupdate()
    # time.sleep(3)

    while(True):
        k = quote_text_window.getch()
        quote_text_window.clear()

        if k == ord('r') or k == ord('R'):
            quote_text_window.addstr('Generating quote...')
            quote_text_window.refresh()
            
            quote_text_window.clear()
            quoteDispaly = getQuotes()
            quote_text_window.addstr(quoteDispaly, c.color_pair(3))
            stdscr.noutrefresh()
            quote_window.noutrefresh()
            quote_text_window.noutrefresh()
            c.doupdate()

        
        elif k == ord('q') or k == ord('Q'):
            break
            # quote_text_window.clear()
            # quote_text_window.addstr('Are you sure want to exit? (Y\\n)')
            # quote_text_window.refresh()


c.wrapper(main)