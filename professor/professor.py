import random


def main():
    int_level = get_level()
    

    int_score = 0
    for i in range(0, 10):
        int_x = generate_integer(int_level)
        int_y = generate_integer(int_level)
        
        for c in range(0, 3):
            if int(input(f"question: {int_x} + {int_y} = ")) == int_x + int_y:
                print("corect")
                int_score += 1
                break
            print("EEE")
            if c == 2:
                print(f"answer: {int_x + int_y}")

    print(f"score = {int_score}")


def get_level():
    int_level = -1
    while int_level < 1 or int_level > 3:
        int_level = int(input("level 1-3\n"))
    return int_level


def generate_integer(level):
    return random.randrange(0, 10**level)


if __name__ == "__main__":
    main()




