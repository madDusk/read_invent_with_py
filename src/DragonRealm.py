#!/usr/bin/env python3

import random

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
    Оригинальное решение :./InventWithPython_resources/dragon.py
"""


print("""
    You are in a land full of dragons. In front of you,
    you see two caves. In one cave, the dragon is friendly
    and will share his treasure with you. The other dragon
    is greedy and hungry, and will eat you on sight.""")

while True :
    print('Which cave will you go into? (1 or 2)')
    choise=input()
    if choise != '1' and choise != '2' :
        print('Oh, oh. Do you speak English?')
        continue
    choise = int( choise )    

    greedydragon = random.randint(1,2)
    if choise == greedydragon :
        print("""You approach the cave...
                 It is dark and spooky...
                 A large dragon jumps out in front of you! He opens his jaws and...
                 Gobbles you down in one bite!""")
    else :
        print("""You approach the cave...
                 It is dark and spooky...
                 A large dragon jumps out in front of you! He opens his jaws and...
                 Gives you his treasure""")

    print('Do you want to play again? (yes or no)')
    answer=input()
    if answer == 'y' or answer == 'yes' :
        continue
    else :
        print('Good bye')
        break

""" Упс, невнимательно прочитал введение.Будет использовано:
    Flowcharts
    Creating your own functions with the def keyword
    Multiline strings
    while statements
    The and, or, and not Boolean operators
    Truth tables
    The return keyword
    Global and local variable scope
    Parameters and arguments
    The sleep() function

Я решал по вчерашнему алгоритму
"""
