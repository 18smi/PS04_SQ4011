import sys
from pyfiglet import Figlet
figlet = Figlet()

if len(sys.argv) == 3:
    if sys.argv[1] != "-f" and sys.argv[1] != "--font":
        print("Invalid usage")
        sys.exit()
    if  sys.argv[2] in figlet.getFonts():
        figlet.setFont(font=sys.argv[2])
    else:
        print("Invalid usage")
        sys.exit()
elif len(sys.argv) != 1:
    print("Invalid usage")
    sys.exit()


string_input = input("words\n")

print(figlet.renderText(string_input))
