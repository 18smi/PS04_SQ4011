import random


def main():
    int_level = get_level()
    

    int_score = 0# holds the current score 
    for i in range(0, 10):# asks 10 questions
        int_x = generate_integer(int_level)
        int_y = generate_integer(int_level)
        
        for c in range(0, 3):# gives 3 chances to answer the question corectly
            if int(input(f"question: {int_x} + {int_y} = ")) == int_x + int_y:# if corect answer
                print("corect")
                int_score += 1# increase the score
                break
            print("EEE")
            if c == 2:# gives answer if the user failed 3 times
                print(f"answer: {int_x + int_y}")

    print(f"score = {int_score}")# prints the score


def get_level():
    int_level = -1
    while int_level < 1 or int_level > 3:# asks for level until user inputs 1, 2 or 3
        int_level = int(input("level 1-3\n"))
    return int_level


def generate_integer(level):
    return random.randrange(0, 10**level)# generates a number between 0 and 10^level


if __name__ == "__main__":
    main()




