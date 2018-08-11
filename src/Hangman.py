#!/usr/bin/env python3

import random


"""
p0nushiK_a
        Hangman game.
    This game is more complicated than our previous games but also more fun.
    Because the game is advanced, we’ll first carefully plan it out by
    creating a flowchart in this chapter. In Chapter 8, we’ll actually write
    the code for Hangman.


    Для версии: Python 3.x.x

    Пример взят здесь:
            http://inventwithpython.com/invent4thed/chapter7.html
    Read online for free:
        "Invent Your Own Computer Games with Python, 4th Edition"
        Chapter 7
    Оригинальное решение :./InventWithPython_resources/hangman.py

    Наскоком не получилось ( Hangman_notwork.py
    Начинаю заново :)

    2018/08/10 02:37:31
    Кажется получилось. Признаюсь часть подсмотрел в оригинале.
    Особенно помогла строка:
    currentBlank = currentBlank[:i] + guess + currentBlank[i+1:]
    Всё ломал голову как изменять строку, если она неизменяемая.
    (Правильно, создать новую с помощью срезов)
    
    NOTE: I'm not speak English. The whole output is
          translated by the  Google     
"""
#########################  FUNCTION ###################################
def Intro() :
    print("""
      #####################   Hangman game.   #########################
    This game is more complicated than our previous games but also more fun.
    Because the game is advanced, we’ll first carefully plan it out by
    creating a flowchart in this chapter. In Chapter 8, we’ll actually write
    the code for Hangman.
    """)

def RandomWord( wordslist ) :
    return wordslist[random.randint(0, len(wordslist)-1)]

def GetGuess( alreadyGuessed) :
    print('Guess letter')
    guess = input()
    guess = guess.lower()
    if len(guess) != 1:
        print('Please enter a single letter')
    elif guess.isdigit() :
        print('Please enter letter')
    elif guess in alreadyGuessed :
        print('You have already guessed that letter. Choose again.')
    else :
        return guess
    return ''

    
#########################   START   ##################################

####### ПОДГОТОВКА ПЕРЕМЕННЫХ ###

# Этот список меня пугает   :0 
hangmanBlanks=[
"""
    +-----+ 
    |     |
    |     
    |    
    |     
    |        
   === """,
"""
    +-----+ 
    |     |
    |     o
    |     
    |     
    |        
   === """,
"""
    +-----+ 
    |     |
    |     o
    |    / 
    |     
    |        
   === """,
"""
    +-----+ 
    |     |
    |     o
    |    /| 
    |     
    |        
   === """,
"""
    +-----+ 
    |     |
    |     o
    |    /|\ 
    |     
    |        
   === """,
"""
    +-----+ 
    |     |
    |     o
    |    /|\ 
    |    /  
    |        
   === """,
"""
    +-----+ 
    |     |
    |     o
    |    /|\ 
    |    / \ 
    |        
   === """]

#  словарь
wordsList = ['ant', 'baboon', 'badger', 'bat', 'bear', 'beaver',
             'camel', 'cat', 'clam', 'cobra', 'cougar', 'coyote',
             'crow', 'deer', 'dog', 'donkey', 'duck', 'eagle',
             'ferret', 'fox', 'frog', 'goat', 'goose', 'hawk',
             'lion', 'lizard', 'llama', 'mole', 'monkey', 'moose',
             'mouse', 'mule', 'newt', 'otter', 'owl', 'panda',
             'parrot', 'pigeon', 'python', 'rabbit', 'ram', 'rat',
             'raven', 'rhino', 'salmon', 'seal', 'shark', 'sheep',
             'skunk', 'sloth', 'snake', 'spider', 'stork', 'swan',
             'tiger', 'toad', 'trout', 'turkey', 'turtle', 'weasel',
             'whale', 'wolf', 'wombat', 'zebra']

#  выбрать случайное слово из списка
secretWord     = RandomWord( wordsList )
currentBlank   = '_'*len( secretWord )
missedLetters  = ''
correctLetters = ''
guessedLetters = 0
hangmanIndex   = 0
count          = 1

print( secretWord )
print( currentBlank )

Intro()
while True :
    guess = GetGuess(missedLetters + correctLetters)

    if not guess : continue
        
    if guess in secretWord :
        correctLetters=correctLetters + guess
        for i in range( len( secretWord ) ) :
            if guess == secretWord[i] :
                currentBlank = currentBlank[:i] + guess + currentBlank[i+1:]
                guessedLetters = guessedLetters + 1
    else :
        missedLetters = missedLetters + guess
        hangmanIndex = hangmanIndex + 1
    
    if hangmanIndex < 6:
        print(hangmanBlanks[hangmanIndex])
        print('   ' + currentBlank)
    else :
        print(hangmanBlanks[hangmanIndex])
        print('   ' + currentBlank)
        print('You lose')
        break

    if guessedLetters == len( secretWord ) :
        print('You Win')
        break

    count = count + 1

print('Number of guessing ' + str(count))
print('Secret word is \'' + secretWord + '\'')
