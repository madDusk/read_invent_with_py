#!/usr/bin/env python3

"""
    Версия два чуть-чуть доработана.  ТАМ
    
    This is a Guess the Number game.
    Программа "загадывает" (генерирует случайное число от 1 до 20. 
    Игрок должен угадать его за 6 ходов
    
    Для версии: Python 3.x.x

    Пример взят здесь:
            http://inventwithpython.com/invent4thed/chapter3.html
    Read online for free:
        "Invent Your Own Computer Games with Python, 4th Edition"
        Chapter 3
    Оригинальное решение :./InventWithPython_resources/guess.py
"""

# подключения модуля random для вызова функции randint()
import random

print('Hello! What is your name?')
name=input()

print('Well, ' + name + '. I am thinking of a number between 1 and 20.')

#сгенерировать случайное число от  1 до 20
num = random.randint( 1, 20 )

# Это мой вариант с циклом while(написан после 2-х дневного изучения)
"""
i=1
while i<=6 :
    print('Take a guess.')

    #обработка ошибочого ввода, если ввели не число
    try:
        uNum = int(input())
    except ValueError:
        print('Sorry, ' + name + ', but maybe your input not number')
        continue
        
    if uNum > num :
        print('Your guess is too high.')
    elif uNum < num :
        print('Your guess is too low.')
    elif uNum == num :
        break
        
    i = i + 1

if i<= 6 :
    print('Good job, ' + name +' You guessed my number ' + str(num) + ' in ' + str(i) + ' guesses!')
else :
    print('Sorry, ' + name + ' Maybe You win in other time!')
    print('Nope. The number I was thinking of was ' + str(num) +'. You  make ' + str(i) + ' guesses!')
"""

# цикл будет выполняться пять раз //за шесть раз обязательно угадешь
# range( 1, 6 ) - возвращает список
for i in range( 1, 6 ):
    print('Take a guess.')

    #обработка ошибочого ввода, если ввели не число
    try:
        uNum = int(input())
    except ValueError:
        print('Sorry, ' + name + ', but maybe your input not number')
        continue
        
    if uNum > num :
        print('Your guess is too high.')
    elif uNum < num :
        print('Your guess is too low.')
    elif uNum == num :
        #неплохо бы оператор goto чтобы сразу перепрыгнуть в конец
        print('Good job, ' + name +' You guessed my number', end=' ')
        break

if uNum != num :
    print('Nope. The number I was thinking of was', end=' ')

# ЗДЕСЬ. последняя часть строки повторялась в любом случае
print( str(num) +'. You  make ' + str(i) + ' guesses!')       
