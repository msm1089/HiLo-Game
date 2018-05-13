import random


def main():
    play = True

    while play:
        game_loop()

        print("Press 'y' to play again, or any other key to exit.")
        play_again = input()
        play = play_again in ('y', 'Y')


def game_loop():
    secret_number = random.randint(1, 100)
    print("Guess the number!")

    while True:
        input_number = input()

        if input_number < secret_number:
            print("That is too low.")
        elif input_number > secret_number:
            print("That is too high.")
        else:
            print("You got it!!!")
            break


if __name__ == '__main__':
    main()
