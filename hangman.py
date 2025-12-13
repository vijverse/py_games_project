def play_hangman():
    word = "vibecheck"
    guessed = "_" * len(word)
    hint = "People say this when they want to know your mood or 'vibes'."
    wrong = 0

    print("Welcome to Hangman")
    print("Type 'hint' for a hint\n")

    while guessed != word and wrong < 6:
        print("Word:", guessed)
        print("Wrong attempts:", wrong)
        ch = input("Enter a letter: ")

        if ch == "hint":
            print("Hint:", hint)
            continue

        if ch in word:
            new = ""
            for i in range(len(word)):
                if word[i] == ch:
                    new += ch
                else:
                    new += guessed[i]
            guessed = new
            print("Nice, correct letter\n")
        else:
            wrong += 1
            print("Wrong letter\n")

    if guessed == word:
        print("You guessed the word:", word)
    else:
        print("You ran out of attempts. The word was:", word)

    input("\nPress Enter to return to the menu...")
