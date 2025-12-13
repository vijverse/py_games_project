
questions = [
    {
        "question": "Which of these animals can sleep standing up?",
        "options": ["A) Dolphins", "B) Horses", "C) Alligators", "D) Snakes"],
        "answer": "B"
    },

    {
        "question": "Which game was the first to be played in outer space?",
        "options": ["A) Chess", "B) Rubik's Cube", "C) Tetris", "D) Uno"],
        "answer": "C"
    },

    {
        "question": "Which of these items was invented first??",
        "options": ["A)Headphones ", "B)Microwave ", "C)Roller coaster ", "D)Sunglasses "],
        "answer": "D"
    },

    {
        "question": "Which drink was originally invented as a medicine?",
        "options": ["A)Coca-Cola ", "B)Fanta ", "C)Lemonade ", "D)Sprite "],
        "answer": "A"
    },

    {
        "question": "Which video game held the Guinness World Record for most sales?",
        "options": ["A)Fortnite ", "B)Minecraft ", "C)GTA V ", "D)GTA V "],
        "answer": "B"
    },

    {
        "question": "Which animal has the largest eyes of any living creature?",
        "options": ["A)Giant Squid ", "B)Giant Squid ", "C)Ostrich ", "D)Whale "],
        "answer": "A"
    },

    {
        "question": "Which movie became the first to make more than $2 billion worldwide?",
        "options": ["A) Avatar", "B) Avengers: Endgame", "C) Titanic", "D) Star Wars"],
        "answer": "A"
    },

    {
        "question": "Which music streaming platform launched first?",
        "options": ["A) Spotify", "B) Apple Music", "C) YouTube Music", "D) SoundCloud"],
        "answer": "D"
    },

    {
        "question": "Which animated movie took the longest to make?",
        "options": ["A) Frozen", "B) Toy Story", "C) The Nightmare Before Christmas", "D) Avatar"],
        "answer": "C"
    },

    {
        "question": "Which book series was originally rejected by publishers 12 times?",
        "options": ["A) Hunger Games", "B) Harry Potter", "C) Divergent", "D) Percy Jackson"],
        "answer": "B"
    },

    {
        "question": "Which country has a vending machine that sells fresh eggs?",
        "options": ["A) Japan", "B) USA", "C) Germany", "D) South Korea"],
        "answer": "A"
    },

    {
        "question": "What part of the human body never stops growing?",
        "options": ["A) Hair", "B) Bones", "C) Nose and ears", "D) Brain"],
        "answer": "C"
    },
]


def play_trivia():
    print("\n Welcome to Trivia!\n")

    score = 0
    total = len(questions)

    for q in questions:  # It shows the user the questions and the options
        print(q["question"])
        for option in q["options"]:
            print(option)

        user = input("Your answer (A/B/C/D): ").strip().upper()
        while user not in ["A", "B", "C", "D"]:
            user = input("Please enter A, B, C, or D: ").strip().upper()

        # Checks if the answer is correct
        if user == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! Correct answer is: {q['answer']}\n")

    # Results
    print(" TRIVIA RESULTS")
    print(f"You scored {score}/{total}!")

    if score == total:
        print("Perfect Score!.")
    elif score >= total * 0.7:
        print("Great job!")
    elif score >= total * 0.4:
        print("Not bad.")
    else:
        print("Better luck next time!")

    input("\nPress Enter to return to the menu...")
