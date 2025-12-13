import random

words = ["nature", "suits", "duckling", "hailstorm", "germany",
"bangalore", "encyclopedia", "challenge"]

def scramble_word(word):
    chars = list(word)
    random.shuffle(chars)
    return ''.join(chars)

def play_game():
    print("Welcome to the Scramble Game!")
    score = 0

    for i in range(len(words)):
        word = random.choice(words)
        scrambled = scramble_word(word)
        print(f"\nScrambled word: {scrambled}")
        guess = input("Your guess: ").strip().lower()

        if guess == word:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The word was: {word}")

    print(f"\nGame Over! Your score: {score}/{len(words)}")
    input("\nPress Enter to return to the menu...")
