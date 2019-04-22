__author__ = 'Ушаков Михаил Викторович'

# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

print("Задача № 1")

equation = 'y = -12x + 11111140.2121'
x = 2.5

# вычислите и выведите y

list_elements = equation.split(" ") # разбиваем формулу на элементы в список
# print(list_elements)
first_element = str(list_elements[2][: 3]) # вычленяем из второго элемента списка переменную Х
second_element = list_elements[-1] # записываем в переменную последний элемент списка
# print(first_element)
coordinate_Y = float(first_element) * x + float(second_element)
print(f"\nКоордината Y точки с заданной координатой x равна:\n{coordinate_Y}")

# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
# date = '01.11.1985'
#
# # Примеры некорректных дат
# date = '01.22.1001'
# date = '1.12.1001'
# date = '-2.10.3001'

print("\nЗадача № 2")

day = input("Введите число: ")
month = input("Введите месяц: ")
year = input("Введите год: ")
date = [day, month, year] # Запишем в список введеные данные
day = int(day)
month = int(month)
year = int(year)
# print(type(year))
lilte_month = [4, 6, 9, 11]# Список месяцев в которых дней меньше 31
leap_years = [] # Пусой список для високосных годов
i = 0
while i < 9999:
    i += 4
    if i != 10000:
        leap_years.append(i) # Формирую список високосных годов
# print(leap_years)
if day > 31 or day < 1:
    print("Такого дня нет!")
elif month > 12 or month < 0:
    print("Такого месяца нет!")
elif year > 9999 or year < 1:
    print("Такого года нет!")
elif month in lilte_month and day > 30:
    print("Такого дня нет в этом месяце!")
elif month == 2 and day > 29 or day < 1:
    print("Такого дня нет в этом месяце!")
elif month == 2 and year not in leap_years and day > 28:
    print("Такого дня нет в этом месяце этого года! Этот год не високосный!")
else:
    print(f"Дата введена правильно! {date[0]}.{date[1]}.{date[2]}")



#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты,
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3

# Не решил(