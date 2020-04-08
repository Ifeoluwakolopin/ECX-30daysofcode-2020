# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 12:20:42 2020

@author: TheAre
"""



def Hangman(trials, word):
    
    ''' This function takes in the number of guesses and a secret word as parameter and
    returns whether or not the user has won/lost the game of Hangman'''
    
    
    print('WELCOME TO THE GAME OF HANGMAN!!')
    print(' ')
    print('''Try to guess all the letters of a secret word known only to me.
As a hint, the secret word has {0} letters in it.
You have {1} trials for this game.
GOODLUCK!'''.format(len(word), trials))
    
    secret_word = list(word.lower())
    guess_word = ''
    
    win_display = "YOU WIN!!, The secret word is {0}".format(word)
    lose_display = 'YOU LOSE. Better Luck Next Time! The secret word is {0}'.format(word)
    
    while trials > 0 :
        guess = input('Guess a Letter: ')
        guess = guess.lower()
        if guess in secret_word:
            print('{0}, You guessed right!'.format(guess))
            i = secret_word.index(guess)
            del secret_word[i]
            guess_word += guess
            trials -= 1
            print ('You have {0} guesses left'.format(trials))
        else:
            if (guess in guess_word) and (guess not in secret_word):
                print('You have guessed all instances of this letter in the secret word already')
                print ('You have {0} guesses left'.format(trials))
            else:
                print('_, That\'s not a correct guess!')
                trials -= 1
                print ('You have {0} guesses left'.format(trials))
       
        if len(word) == len(guess_word):
            return win_display
            break;
        if trials == 0 and (len(guess_word) != len(secret_word)):
            return lose_display
        
trials = 10
word = 'satires'

print(Hangman(trials, word))

