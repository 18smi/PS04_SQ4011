name_list = []
try:
    while True:
        name_list.append(input("name\n"))

except EOFError:
    print(f"adieu, adieu, to {name_list[0]}", end='')
    for i in range(1, len(name_list) - 1):
        print(f", {name_list[i]}", end='')
    print(f" and {name_list[len(name_list)-1]}")
