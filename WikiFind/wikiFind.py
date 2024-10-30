#!python3

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
  search = ' '.join(sys.argv[1:])
else:
  search = pyperclip.paste()

webbrowser.open('https://en.wikipedia.org/wiki/' + search)