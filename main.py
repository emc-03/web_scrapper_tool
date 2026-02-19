#python3
#mapIT.py
import webbrowser, sys

from pyperclip import paste

if len(sys.argv) > 1:
    #Get Address from command line
    address = ''.join(sys.argv[1:])
else:
    #Get Address from clipboard
    address = paste()
webbrowser.open('https://www.google.com/maps')


