import random

def hangman_game():
    words = ["spiderman", "dog", "bird", "python"]
    random_word = random.choice(words)
    guessed_word = ["_"] * len(random_word)
    guessed_letters = []
    steps = 6

    

    while steps > 0:
        guess = input("Введите букву: ").lower()
        if len(guess) >2 :
            print("Пожалуйста, введите только одну букву.")
            continue
        if guess in guessed_letters:
            print("Вы уже пробовали эту букву. Попробуйте снова.")

        guessed_letters.append(guess)
        

        if guess in random_word:
            for i in range(len(random_word)):
                if random_word[i] == guess:
                    guessed_word[i] = guess
            print("Хорошо! " + " ".join(guessed_word))
        else:
            steps -= 1
            print(f"Неправильно! Осталось попыток: {steps}")

        display_hangman(steps)

        if "_" not in guessed_word:
            print("Поздравляю! Вы угадали слово: " + random_word)
            break
    else:
        print(f"Вы проиграли! Слово было: {random_word}")

def display_hangman(attempts):
    hangman_states = [
        '''
         -----
         |   |
             |
             |
             |
             |
        =========
        ''',
        '''
         -----
         |   |
         O   |
             |
             |
             |
        =========
        ''',
        '''
         -----
         |   |
         O   |
         |   |
             |
             |
        =========
        ''',
        '''
         -----
         |   |
         O   |
        /|   |
             |
             |
        =========
        ''',
        '''
         -----
         |   |
         O   |
        /|\\  |
             |
             |
        =========
        ''',
        '''
         -----
         |   |
         O   |
        /|\\  |
        /    |
             |
        =========
        ''',
        '''
         -----
         |   |
         O   |
        /|\\  |
        / \\  |
             |
        =========
        '''
    ]

    print(hangman_states[6 - attempts])


hangman_game()
