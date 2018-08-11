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
            http://inventwithpython.com/invent4thed/chapter5.html
    Read online for free:
        "Invent Your Own Computer Games with Python, 4th Edition"
        Chapter 7
    Оригинальное решение :./InventWithPython_resources/dragon.py

    По совету сначала нарисовал схему-алгоритм работы программы,
    но получилось не совсем. Совсем не получилось.
    Оригинальная схема hangman.jpg

    Пока продумываешь какие переменные нужны и даешь им имена
    потихоньку прортсовывается картина будущей программы

    И отлаживать прекрасно (правда особо не  чем сравнить).
    Читает построчно, соответственно и выводит не список ошибок,
    а одну текущую.
    
    NOTE: I'm not speak English. The whole output is
          translated by the  Google

    2018/08/09 13:35:40  Oops, внесение изменений приводит к
    новым ошибкам. Это надо записать

    2018/08/09 23:20:38 ничего не получается. начинаю заново
    Всё переделать к чертовой матери    
"""


def CheckLetter( letter, letterIn ) :
    if letter not in letterIn :
        letterIn.append( letter )
        return False
    return True

def CheckWord( letter, guessword, progressblank ) :
    if letter in guessword :
        for i in range(len(guessword)) :
            if letter == guessword[i] :
                progressblank[i] = letter
    else :
        return False
    return True
    
def GetWord( progressblank) :
    progressword = ''
    for i in range( len(progressblank) ) :
        progressword.join(progressblаnk[i])
    #print (progressword)
    return progressword
   
#########################     START ##################################

####### ПОДГОТОВКА ПЕРЕМЕННЫХ ###
"""
#  подготовить список ( оригинальный список сразу не долистал до конца,
#  а в конце метод split. Конечно так проще, не надо печатать ',' но не
#  непонятно.
#wordsList = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()
"""
#  переписал сразу списком (хоть видно)
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
# len( wordsList ) - возвращает размер списка.
# len( wordsList )-1 - индексация с нуля
i = random.randint( 0, len( wordsList )-1) 
#выбранное слово
guessWord = wordsList[i]                                              

#текущее прогресс. Для вывода угаданных букв (или не угаданных)
progressBlank = []
progressWord = ''

# инициализировать все значения списка тире
for i in range(len(guessWord)) :
    progressBlank.append('-')
    #progressWord += '-'


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

# как чувствует себя человечек (пока не плохо)
currentBlank = 0

""" ДЛЯ отладки какой вывод пока получается
print( hangmanBlanks[currentBlank])
print( progreessWord )
"""

# список уже введённых букв (пока пустой)
letterIn = []
# счетчик попыток
count = 0

#  поехали. PrintIntro
print("""
      #####################   Hangman game.   #########################
    This game is more complicated than our previous games but also more fun.
    Because the game is advanced, we’ll first carefully plan it out by
    creating a flowchart in this chapter. In Chapter 8, we’ll actually write
    the code for Hangman.
    """)
"""#DEBUG guess word
print( guessWord )
print(progressWord)
"""
"""
начать считывание до бесконечности (пока)

2018/08/09 13:44:30
до бесконечности не получится - ограниечением является
размер hangmanBlanks (иначе ошибка)
"""
while currentBlank<6 :
    print( guessWord )
    print(progressWord)
    print('Which your letter ?')
    letter = input()
    if letter.isalpha() and len( letter) == 1 :
        resCheck = CheckLetter( letter, letterIn )
        if resCheck :
            print('This letter has already been entered')
            print(letterIn)
            continue
    
        resCheck = CheckWord( letter, guessWord, progressBlank )
        if resCheck :
            print(hangmanBlanks[currentBlank])
            print(*progressWord)
        else :
            currentBlank = currentBlank + 1
            print(hangmanBlanks[currentBlank])
            print(progressWord)
        
    
    if currentBlank == 5 :
        print('I\'m tired, I give a hint.Word is ==> ' + guessWord)
"""
letterIn = []
for i in range( len(progressWord)) :
    letterIn.append( progressWord[i])

print( letterIn )

letterIn = progressWord
"""
"""if guessWord == progressWord :
    print('Yor WIN')
else :
    print('Sorry, maybe anytime')
"""
