# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.


a = int (input('первый элемент прогрессии = ')) # Введение первого элемента прогрессии.
d = int (input('разница прогрессии = '))       # Введение разницы прогрессии.
n = int (input('длина масива = '))            # Введение длинны массива.
mas = []                                   #пустой массив
print ("массив:  ")                       #вывод сообщения
for i in range (n):                     #цикл создания массива
    mas.append (a)                      #создание массива
    print (mas [i], end = " ")          #вывод элементов массива
    a = a + d                           #вычисление члена прогрессии

# первый элемент прогрессии = 3
# разница прогрессии = 7
# длина масива = 5
# массив:
# 3 10 17 24 31