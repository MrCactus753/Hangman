# Write your code here
from random import choice
from string import ascii_lowercase


def game():
    #different variables
    print('H A N G M A N\n')
    words = ['python', 'java', 'kotlin', 'javascript']
    used_word = choice(words)
    part_word = list('-' * len(used_word))
    used_letters = []
    tries = 8

    #main game loop
    while tries > 0:
        print('\n')
        print(''.join(part_word))
        user_input = input('Input a letter: ')

        if len(user_input) == 1:
            if user_input in ascii_lowercase:
                for i in range(len(used_word)):
                    if user_input == used_word[i]:
                        part_word[i] = user_input
                if user_input in used_letters:
                    print('You already typed this letter')
                elif user_input not in used_word or user_input == '':
                    tries -= 1
                    used_letters.append(user_input)
                    print('No such letter in the word')
                else:
                    used_letters.append(user_input)
            else:
                print("It is not an ASCII lowercase letter ")
        else:
            print("You should print a single letter")
    if part_word == used_word:
        print("You guessed the word!\nYou survived!")
    else:
        print('You are hanged!')


def main():
    while True:
        main_input= input('Type "play" to play the game, "exit" to quit:')
        if main_input =='play':
            game()
        elif main_input =='exit':
            break
        else:
            pass


main()
