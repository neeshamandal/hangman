import random
from WORDS import word_list


def get_word():
    word = random.choice(word_list)
    return word.upper()


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("lets play HANGMAN!")
    print("the length of the word is",len(word))
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("please guess the name of our family member: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("you already guessed the letter: ")
                tries -= 1
                guessed_letters.append(word)
                print("only", tries,"chances left")
            elif guess not in word:
                print(guess, "not in the word: ")
                tries -= 1
                guessed_letters.append(word)
                print("only",tries, "chances left")


            else:
                print("good job", guess, "is the letter")
                print("only",tries,"chance left")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index1 in indices:
                    word_as_list[index1] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True

        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("you have already guessed the word", guess)
            elif guess != word:
                print(guess,"is not the word: ")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word

        else:
            print("not a valid guess: ")
            print(tries,"left")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")

    if guessed:
        print("congrats you guessed the word, you win")
    else:
        print("sorry you ran out of tries, the word was", word)







def display_hangman(tries):
        stages = [  # final state: head, torso, both arms, and both legs
            """
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |     / \\
               -
            """,
            # head, torso, both arms, and one leg
            """
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |     / 
               -
            """,
            # head, torso, and both arms
            """
               --------
               |      |
               |      O
               |     \\|/
               |      |
               |      
               -
            """,
            # head, torso, and one arm
            """
               --------
               |      |
               |      O
               |     \\|
               |      |
               |     
               -
            """,
            # head and torso
            """
               --------
               |      |
               |      O
               |      |
               |      |
               |     
               -
            """,
            # head
            """
               --------
               |      |
               |      O
               |    
               |      
               |     
               -
            """,
            # initial empty state
            """
               --------
               |      |
               |      
               |    
               |      
               |     
               -
            """
        ]
        return stages[tries]


def main():
    word = get_word()
    play(word)
    while input("play again? (Y/N)").upper() == "Y":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()


