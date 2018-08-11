#!/usr/bin/env python3

import random
import time

"""
    DRAGON REALM

    How to Play Dragon Realm

In this game, the player is in a land full of dragons. The dragons all live
in caves with their large piles of collected treasure. Some dragons are
friendly and share their treasure. Other dragons are hungry and eat anyone
who enters their cave. The player approaches two caves, one with a friendly
dragon and the other with a hungry dragon, but doesn’t know which dragon is
in which cave. The player must choose between the two.
    
    Для версии: Python 3.x.x

    Пример взят здесь:
            http://inventwithpython.com/invent4thed/chapter5.html
    Read online for free:
        "Invent Your Own Computer Games with Python, 4th Edition"
        Chapter 5
    Оригинальное решение :../src_original/dragon.py

    При объявлении функции и её вызове без параметров требуется всё равно
    использовать скобки. Иначе считает, что это переменная :(

    Функция должна быть описана перед её вызовом

    return возвращает значение (а можно несколько return'ов?)
"""

def PrintIntro() :
    print("""
        You are in a land full of dragons. In front of you,
        you see two caves. In one cave, the dragon is friendly
        and will share his treasure with you. The other dragon
        is greedy and hungry, and will eat you on sight.
        """)
        
# Получить выбор пользователя
def GetChoose() :
    
    while True:
        print('Which cave will you go into? (1 or 2)')
        choose=input()
        if choose == '1' or choose == '2' :
            break
        else :
            print('Oh, oh. Do you speak English?')
            continue
                       
    return int(choose)


# Нагнетаю обстановку,         
def DragonDo() :
    print("You approach the cave...")
    time.sleep( 2 )
    print("It is dark and spooky...")
    time.sleep( 2 )
    print("A large dragon jumps out in front of you! He opens his jaws and...")
    time.sleep( 2 )

# функции передаётся два параметра (ради эксперимента)
def CheckCave( chooseCave, greedyDragon ) :
    if chooseCave == greedyDragon :
        #вызов функции определённой выше
        DragonDo()
        print('Gobbles you down in one bite!')
    else :
        DragonDo()
        print('Gives you his treasure')

print('####################    START GAME    ########################')
    
while True :
    PrintIntro()
    CheckCave( GetChoose(), random.randint(1,2) )
    
    print('\n\nDo you want to play again? ( y(yes) or any key )')
    answer=input()
    if answer == 'y' or answer == 'yes' :
        continue
    else :
        print('Good bye')
        break
        
################## It's all Folks #################################        
