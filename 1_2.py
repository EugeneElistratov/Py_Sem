# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, 
# что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# *Пример:*

# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10

num = int(input("Введите количество журавликов S ->: "))

Petya = (num // 3) // 2
Seroja = (num // 3) // 2
Katya = (Petya + Seroja) * 2

print (Petya,  Katya,  Seroja)