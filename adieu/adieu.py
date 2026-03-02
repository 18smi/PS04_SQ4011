name_list = []# holds the list of inputed names
try:
    while True:
        name_list.append(input("name\n"))# adds the input to the list until the user inputs crtl+D

except EOFError:# prints in desired format
    print(f"adieu, adieu, to {name_list[0]}", end='')
    for i in range(1, len(name_list) - 1):
        print(f", {name_list[i]}", end='')
    if (len(name_list) != 1):
        print(f" and {name_list[len(name_list)-1]}")
    else:
        print()# if only one name, adds a new line
