import random

int_level = -1
while int_level <= 0:# asks for level untill a positive non-zero int is given
    int_level = int(input("level\n"))

int_target = random.randrange(1, int_level)# selects a random target between 1 and the target (inclusive)

while True:# starts game loop
    int_guess = int(input("guess\n"))# exepts a guess
    if int_guess < int_target:# if guess is to small
        print("to small")
    elif int_guess > int_target:# if guess is to large
        print("to big")
    else:# if guess is spot on
        print("just right")
        break