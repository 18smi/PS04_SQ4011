import random

int_level = -1
while int_level <= 0:
    int_level = int(input("level\n"))

int_target = random.randrange(1, int_level)

while True:
    int_guess = int(input("guess\n"))
    if int_guess < int_target:
        print("to small")
    elif int_guess > int_target:
        print("to big")
    elif int_guess == int_target:
        print("just right")
        break