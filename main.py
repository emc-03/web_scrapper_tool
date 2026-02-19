#python3
#mapIT.py
import webbrowser, sys
if len(sys.argv) > 1:
    #Get Address from command line
    address = ''.join(sys.argv[1:])
#TODO: Get address from clipboard