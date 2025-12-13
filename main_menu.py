from trivia import play_trivia
from scramble import play_game
from hangman import play_hangman

def main_menu():
    while True:
        print("\n WELCOME TO PY GAMES")
        print("1) Trivia")
        print("2) Scramble")
        print("3) Hangman")
        print("4) Quit")

        choice = input("Choose a game (1-4): ").strip()

        if choice == "1":
            play_trivia()
        elif choice == "2":
            play_game()
        elif choice == "3":
            play_hangman()
        elif choice == "4":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main_menu()
