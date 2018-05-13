import random


def main():
    play = True

    while play:
        game_loop()

        print("Press 'y' to play again, or any other key to exit.")
        play_again = input()
        play = play_again in ('y', 'Y')


def game_loop():
    secret_number = get_secret_number()
    print("Guess the number!")

    while True:
        input_number = input()

        if input_number < secret_number:
            print("That is too low.")
        elif input_number > secret_number:
            print("That is too high.")
        else:
            print("You got it!!!")


def get_secret_number():
    secret_number = random.randint(1, 100)
    return secret_number


if __name__ == '__main__':
    main()
