import sys
from pyfiglet import Figlet
figlet = Figlet()

if len(sys.argv) == 3:
    if sys.argv[1] != "-f" and sys.argv[1] != "--font":# fail condition
        print("Invalid usage")
        sys.exit()
    
    if  sys.argv[2] in figlet.getFonts():# if font is given, set the font
        figlet.setFont(font=sys.argv[2])
    else:# invaled font
        print("Invalid usage")
        sys.exit()

elif len(sys.argv) != 1:# if len(argv) != 1 and != 3, exit
    print("Invalid usage")
    sys.exit()


print(figlet.renderText(input("words\n")))# prints the input rendered by figlet