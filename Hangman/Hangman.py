import random
while True:
    #word = input("Enter a word or press ENTER to exit: ")
    raw_pool = open(
        "C:\\Users\\pmick\\OneDrive\\Pulpit\\Python\\Hangman\\ukenglish.txt", "r")
    pool = [line for line in raw_pool.readlines()]
    rand = random.randint(0, len(pool))
    word = pool[rand].replace("\n", "").upper()
    # print("\n\n\n\n\n\n\n")
    # if word == "":
    #    exit()
    if word.isalpha() and len(word) >= 3:
        word = list(word)

        no_guesses = 10

        def hanging_process():
            if no_guesses == 10:
                print('''
                
                ''')
            elif no_guesses == 9:
                print('''
                ___________
                ''')
            elif no_guesses == 8:
                print('''
                 |
                 |
                 |
                 |
                 |
                 |
                ___________ 
                ''')
            elif no_guesses == 7:
                print('''
                 ________
                 |
                 |
                 |
                 |
                 |
                 |
                ___________
                ''')
            elif no_guesses == 6:
                print('''
                 ________
                 |      |
                 |
                 |
                 |
                 |
                 |
                ___________
                ''')
            elif no_guesses == 5:
                print('''
                 ________
                 |      |
                 |      0
                 |
                 |
                 |
                 |
                ___________
                ''')
            elif no_guesses == 4:
                print('''
                 ________
                 |      |
                 |      0
                 |      |
                 |      |
                 |
                 |
                ___________
                ''')
            elif no_guesses == 3:
                print('''
                 ________
                 |      |
                 |      0
                 |     /|
                 |      |
                 |
                 |
                ___________
                ''')
            elif no_guesses == 2:
                print('''
                 ________
                 |      |
                 |      0
                 |     /|\\
                 |      |
                 |
                 |
                ___________
                ''')
            elif no_guesses == 1:
                print('''
                 ________
                 |      |
                 |      0
                 |     /|\\
                 |      |
                 |     /
                 |
                ___________
                ''')

        masked = ['_' for let in range(len(word))]
        guessed = set()
        # masked = ['_'] * len(word)

        print(masked)

        while no_guesses > 0:
            print("Guesses left: ", no_guesses, "\n")
            guess = input("Guess the letters or press ENTER to exit: ").upper()
            if guess == "":
                exit()
            if guess.isalpha() and len(guess) == 1:
                if guess in word:
                    index = -1
                    while True:
                        try:
                            index = word.index(guess, index + 1)
                            masked[index] = guess
                        except:
                            break
                    print(str(masked))
                    hanging_process()
                    if guessed != set():
                        print("Wrong guesses: " + str(guessed))
                    if masked == word:
                        print("VICTORY")
                        break
                elif guess in guessed:
                    print('You have already guessed this letter.')
                else:
                    print(str(masked))
                    no_guesses -= 1
                    guessed.add(guess)
                    hanging_process()
                    print("Wrong guesses: " + str(guessed))
            else:
                print("Invalid character(s) detected or input too long")
                print(str(masked))
                hanging_process()
        else:
            print("GAME OVER")
            print('''
              ________
              |      |
              |      0
              |     /|\\
              |      |
              |     / \\
              |
            ___________
            ''')
            print(str(word))
    else:
        print("Invalid characters detected.")

'''
Things to add:
> GUI
> possibly a multiplayer server
'''
